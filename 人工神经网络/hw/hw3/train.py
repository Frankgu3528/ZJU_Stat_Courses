import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import tqdm
from torchnet import meter

learning_rate = 1e-5
num_layers = 3
epochs = 100
batch_size = 64
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
embedding_dim = 128
hidden_dim = 256

start_words = '钟山风雨起苍黄'  # 诗歌开始
maxlen = 64  # 超过这个长度的之后字被丢弃，小于这个长度的在前面补空格
max_gen_len = 64  # 生成诗歌最长长度

class PoetryModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(PoetryModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, self.hidden_dim, num_layers)
        self.linear1 = nn.Linear(self.hidden_dim, vocab_size)

    def forward(self, input, hidden=None):
        seq_len, batch_size = input.size()
        if hidden is None:
            #  h_0 = 0.01*torch.Tensor(2, batch_size, self.hidden_dim).normal_().cuda()
            #  c_0 = 0.01*torch.Tensor(2, batch_size, self.hidden_dim).normal_().cuda()
            h_0 = input.data.new(num_layers, batch_size, self.hidden_dim).fill_(0).float()
            c_0 = input.data.new(num_layers, batch_size, self.hidden_dim).fill_(0).float()
        else:
            h_0, c_0 = hidden
        # size: (seq_len,batch_size,embeding_dim)
        embeds = self.embeddings(input)
        # output size: (seq_len,batch_size,hidden_dim)
        output, hidden = self.lstm(embeds, (h_0, c_0))

        # size: (seq_len*batch_size,vocab_size)
        output = self.linear1(output.view(seq_len * batch_size, -1))
        return output, hidden
    
def generate(model, start_words, ix2word, word2ix, prefix_words=None):
    """
    给定几个词，根据这几个词接着生成一首完整的诗歌, 比如
    start_words：u'春潮带水晚来急'
    """    
    results = list(start_words)
    start_word_len = len(start_words)
    # 手动设置第一个词为<START>
    input = torch.Tensor([word2ix['<START>']]).view(1, 1).long()
    input = input.to(device)
    hidden = None

    if prefix_words:
        for word in prefix_words:
            output, hidden = model(input, hidden)
            input = input.data.new([word2ix[word]]).view(1, 1)

    for i in range(max_gen_len):
        output, hidden = model(input, hidden)

        if i < start_word_len: 
            w = results[i]
            input = input.data.new([word2ix[w]]).view(1, 1)
        else:
            top_index = output.data[0].topk(1)[1][0].item()
            w = ix2word[top_index]
            results.append(w)
            input = input.data.new([top_index]).view(1, 1)
        if w == '<EOP>':
            del results[-1]
            break
    return results
data = np.load('tang.npz', allow_pickle=True)
word2ix = data['word2ix'].item()
ix2word = data['ix2word'].item()
data_train = torch.from_numpy(data['data'])

dataloader = torch.utils.data.DataLoader(data_train, batch_size=batch_size, shuffle=True, num_workers=2)
model = PoetryModel(len(word2ix), embedding_dim, hidden_dim).to(device)
model.load_state_dict(torch.load('checkpoints_new.pth'))
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss()

loss_meter = meter.AverageValueMeter()
for epoch in range(epochs):
    loss_meter.reset()
    loss = 0
    for batch_idx, data_ in tqdm.tqdm(enumerate(dataloader)):
        data_ = data_.long().transpose(1, 0).contiguous()
        data_ = data_.to(device)
        optimizer.zero_grad()
        input_, target = data_[:-1, :], data_[1:, :]
        output, _ = model(input_)
        loss = criterion(output, target.view(-1))
        loss.backward()
        optimizer.step()

        loss_meter.add(loss.item())

    if (1 + epoch) % 20 == 0:
        # 诗歌原文
        # poetrys = [[ix2word[_word] for _word in data_[:, _iii].tolist()]
        #                 for _iii in range(data_.shape[1])][:16]
        gen_poetries = []  # 分别以这几个字作为诗歌的第一个字，生成8首诗
        for word in list(u'春江花月夜凉如水'):
            gen_poetry = ''.join(generate(model, word, ix2word, word2ix))
            gen_poetries.append(gen_poetry)
        print(gen_poetries)

    if batch_idx % 900 == 0:
        print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch+1, batch_idx * len(data_[1]), len(dataloader.dataset),
                100. * batch_idx / len(dataloader), loss.item()))    
    # save every 100 epoc
    print("epoch",epoch," loss = ",loss.item())
    if (epoch+1) % 25 == 0:
        # torch.save(model.state_dict(), '%s/%s.pth' % ('checkpoints', epoch+1))
        torch.save(model.state_dict(),f'/data/pyc/ggf/poem/checkpoints_{200+epoch+1}.pth')
        print("model saved!")
print("finish training!")

torch.save(model.state_dict(),'/data/pyc/ggf/poem/checkpoints_new.pth')
model.load_state_dict(torch.load("/data/pyc/ggf/poem/checkpoints_new.pth", map_location=device))
start_words = start_words.replace(',', u'，').replace('.', u'。').replace('?', u'？')
lst = generate(model, start_words, ix2word, word2ix)
str = ""
for i in range(len(lst)):
    if (i+1) % 32 != 0:
        str +=lst[i]
    else :
        print(str+"。")
        str = ""
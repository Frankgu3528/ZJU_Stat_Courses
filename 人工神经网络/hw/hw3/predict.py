import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import tqdm
from torchnet import meter

learning_rate = 1e-5
# weight_decay = 1e-4
epochs = 10
batch_size = 256
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

start_words = "钟山风雨起苍黄" # 诗歌开始
maxlen = 128 # 超过这个长度的之后字被丢弃，小于这个长度的在前面补空格
max_gen_len = 64  # 生成诗歌最长长度

class PoetryModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(PoetryModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, self.hidden_dim, num_layers=3)
        self.linear1 = nn.Linear(self.hidden_dim, vocab_size)

    def forward(self, input, hidden=None):
        seq_len, batch_size = input.size()
        if hidden is None:
            #  h_0 = 0.01*torch.Tensor(2, batch_size, self.hidden_dim).normal_().cuda()
            #  c_0 = 0.01*torch.Tensor(2, batch_size, self.hidden_dim).normal_().cuda()
            h_0 = input.data.new(3, batch_size, self.hidden_dim).fill_(0).float()
            c_0 = input.data.new(3, batch_size, self.hidden_dim).fill_(0).float()
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
    print("start_words=",start_words," perfix_words=",prefix_words)
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
            # print(top_index)
            w = ix2word[top_index]
            results.append(w)
            input = input.data.new([top_index]).view(1, 1)
        if w == '<EOP>':
            del results[-1]
            break
    str = ""
    for i in range(len(results)):
        if (i+1) % 16 != 0:
            str +=results[i]
        else :
            print(str+"。")
            str = ""
    # return results
def gen_acrostic(model, start_words, ix2word, word2ix, prefix_words=None):
    """
    生成藏头诗
    start_words : u'深度学习'
    生成：
    深木通中岳，青苔半日脂。
    度山分地险，逆浪到南巴。
    学道兵犹毒，当时燕不移。
    习根通古岸，开镜出清羸。
    """
    results = []
    start_word_len = len(start_words)
    input = (torch.Tensor([word2ix['<START>']]).view(1, 1).long())
    input = input.to(device)
    hidden = None

    index = 0  # 用来指示已经生成了多少句藏头诗
    # 上一个词
    pre_word = '<START>'

    if prefix_words:
        for word in prefix_words:
            output, hidden = model(input, hidden)
            input = (input.data.new([word2ix[word]])).view(1, 1)

    for i in range(max_gen_len):
        output, hidden = model(input, hidden)
        top_index = output.data[0].topk(1)[1][0].item()
        w = ix2word[top_index]

        if (pre_word in {u'。', u'！', '<START>'}):
            # 如果遇到句号，藏头的词送进去生成

            if index == start_word_len:
                # 如果生成的诗歌已经包含全部藏头的词，则结束
                break
            else:
                # 把藏头的词作为输入送入模型
                w = start_words[index]
                index += 1
                input = (input.data.new([word2ix[w]])).view(1, 1)
        else:
            # 否则的话，把上一次预测是词作为下一个词输入
            input = (input.data.new([word2ix[w]])).view(1, 1)
        results.append(w)
        pre_word = w
    return results
data = np.load('tang.npz', allow_pickle=True)
word2ix = data['word2ix'].item()
ix2word = data['ix2word'].item()
model = PoetryModel(len(word2ix), 128, 256).to(device)
model.load_state_dict(torch.load("checkpoints_new_500.pth", map_location=device))
start_words = start_words.replace(',', u'，').replace('.', u'。').replace('?', u'？')

generate(model, start_words, ix2word, word2ix)
generate(model, start_words, ix2word, word2ix,"折柳春色长亭")
generate(model, start_words, ix2word, word2ix,"梧桐寂寞花落")
generate(model, start_words, ix2word, word2ix,"小桥流水人家")
generate(model, start_words, ix2word, word2ix,"天生我材有用")
generate(model, start_words, ix2word, word2ix,"金戈铁马如虎")
generate(model, start_words, ix2word, word2ix,"北风卷地草折")
generate(model, start_words, ix2word, word2ix,"大漠孤烟长河")

import torch
from torch import nn

class SentimentLSTM(nn.Module):
    def __init__(
      self, 
      vocab_size, embed_dim, 
      hidden_dim, n_layers, output_dim
    ):
        super().__init__()
        
        self.vocab_size = vocab_size  
        self.hidden_dim = hidden_dim

        self.n_layers = n_layers 

        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(
            embed_dim, hidden_dim, 
            n_layers, batch_first=True, 
        )
        self.fc = nn.Linear(hidden_dim, output_dim)


    def forward(self, inputs):
        # Embedding: (batch_size, seq_n, D)
        embed_words = self.embedding(inputs)

        # out: (batch_size, seq_n, H)
        out, h = self.lstm(embed_words)
        out = out.contiguous().view(-1, self.hidden_dim)
  
        # fc_out: (batch_size*seq_n, 1)
        fc_out = self.fc(out)
        fc_out = torch.sigmoid(fc_out)
        # fc_out: (batch_size, seq_n)
        fc_out = fc_out.view(embed_words.shape[0], -1) 

        # fc_out: (batch_size, 1)
        sigmoid_last = fc_out[:, -2:-1].squeeze(dim=1)

        return sigmoid_last, h

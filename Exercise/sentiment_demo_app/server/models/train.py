import pandas as pd
import numpy as np
import json

import torch
from torch import nn
from torch import optim

from dataloader import build_data_loader
from lstm  import SentimentLSTM

def load_data():
  cleaned_df = pd.read_csv('./data/cleaned_review.csv', header=None)
  
  with open('./data/word_id.json') as f:
    word_id = json.load(f)

  encoded_corpus = cleaned_df.iloc[:, :-1].values
  label = cleaned_df.iloc[:, -1].values

  return encoded_corpus, label, word_id


def training():
  encoded_corpus, label, word_id = load_data()

  train_loader, valid_loader, test_loader = build_data_loader(encoded_corpus, label, batch_size=1)

  parameters = {
    'vocab_size': len(word_id),
    'embed_dim': 30,
    'hidden_dim': 100,
    'n_layers': 1,
    'output_dim': 1
  }

  model = SentimentLSTM(**parameters)
  print('==== model ====')
  print(model)
  print('==== model parameters ====')
  for n, p in model.named_parameters():
    print(n, p.shape)


  print('==== Start Training ====')
  epoches = 5
  loss_fn = nn.BCELoss()
  optimizer = optim.Adam(model.parameters(), lr = 0.001)
  # prev_valid_loss = 99999

  for epoch in range(epoches):
      for inputs, t_label in train_loader:
          out, _ = model(inputs)
          loss = loss_fn(out, t_label)

          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
      
      # evaluation
      model.eval()
      valid_loss = []
      for inputs, v_label in valid_loader:
          v_out, _ = model(inputs)
          v_loss = loss_fn(v_out, v_label)
          valid_loss.append(v_loss.item())
      model.train()
      
      
      mean_valid_loss = np.mean(valid_loss)
      print('Epoch %d, train loss: %.4f, valid loss: %.4f' % (epoch, loss.item(), mean_valid_loss))

      # early stopping
      # if mean_valid_loss > prev_valid_loss:
      #   print('==== Training Done ====')
      #   break
      # else:
      #   prev_valid_loss = mean_valid_loss


  # test
  model.eval()
  test_loss = []
  toal_correct=0
  for inputs, v_label in test_loader:
      v_out, _ = model(inputs)        
      v_loss = loss_fn(v_out, v_label)
      test_loss.append(v_loss.item())        

      pred_label = torch.round(v_out)
      batch_correct = pred_label.eq(v_label.view_as(pred_label)).sum()
      toal_correct += batch_correct
  print("Test Loss: {:.4f}".format(np.mean(test_loss)))
  print("Test Accuracy: {:.2f}".format(toal_correct/len(test_loader.dataset)))
      
  # save
  torch.save(model.state_dict(), 'model.pkl')

  with open('./parameters.json', 'w') as f:
        json.dump(parameters, f)


if __name__ == '__main__':
  training()

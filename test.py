# -*- coding: utf-8 -*-
"""test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yH2IXSLmyWMaP9CdZGv71UQh9Fy9f933
"""

# 테스트
model.eval()
with torch.no_grad():
    inputs = test_X.to(device)
    targets = test_y
    
    outputs = model(inputs)
    outputs = scaler.inverse_transform(outputs.cpu().numpy())
    
    mae = mean_absolute_error(test_target[seq_length:], outputs)
    print(f'Test MAE: {mae}')
from data_transformation import transform_data
import torch

def save_artifact():
    model_dataset = transform_data()
    # torch.save(model_dataset, "test.pt")
    # model_dataset = torch.load('test.pt')
    with open('model_dataset.pkl', 'wb') as f:
        pickle.dump(model_dataset, f)
    return model_dataset

import numpy as np

# class button pengolahan citra
class pengolahan_citra():
    def __init__(self):
        pass
    
    # konvolusi manual dengan numpy
    def konvolusi_manual(self, input_matrix: np.array, kernel: np.array)-> list[np.array, int]:
        # definisikan shape
        input_h, input_w = input_matrix.shape
        kernel_h, kernel_w = kernel.shape
        
        # Output size
        output_h = input_h - kernel_h + 1
        output_w = input_w - kernel_w + 1
        output = np.zeros((output_h, output_w))
        
        # Proses konvolusi
        for i in range(output_h):
            for j in range(output_w):
                region = input_matrix[i:i+kernel_h, j:j+kernel_w]
                output[i, j] = np.sum(region * kernel)
        
        return [output,int]
    

if __name__ == "__main__":
    print ("weksasda")
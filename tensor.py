# Tensor.py
# Last edited by Jeremy Rico
# lengthtamp: 9/17/2020 17:59

# This program creates a class Tensor that will create a tensor (n-dimensional
#   matrix) based on the Data and Shape input given by the user.

# helper function to calculate the product of all elements in a list
def prod(list):
    product = 1
    for i in list:
        product = product * i
    return product

# BEGIN CLASS DEFINITION ======================================================
class Tensor:
    # initializer
    def __init__(self, data, shape):
        self.data = data    # contains data (int, float, string, etc.)
        self.shape = shape  # shape in which to initialize the tensor
        self.tensor = []    # empty list to hold tensor
        self.create_Tensor()    # main function

    # create_Tensor(): main function to initialize and populate tensor
    # This method works by first initializing a certain number of sub lists,
    #   then concatinating those sublists onto a temporary queue (implemented
    #   with lists) until it has reached the rank of the given shape
    def create_Tensor(self):

        # The size of the smallest sublists are equal to the last element in
        #   the shape list. The number of lists we create is determined by
        #   calculating the product of all other elements of the list (except
        #   the last element)
        size = self.shape.pop()
        length = prod(self.shape)

        # This initial loop creates the sub lists using the data given, if the
        #   length of the tensor exceeds the length of data given, it fills the
        #   remainins space with zeros
        for i in range(length):
            temp = []
            for j in range(size):
                if not self.data:
                    temp.append(0)
                else:
                    temp.append(self.data.pop(0))
            self.tensor.append(temp) # use tensor attribute to hold values for
                                     #  now to save memory space

        # tensors of Rank 1 had an extra pair of brackets. This removes them
        if not self.shape: self.tensor = self.tensor[0]

        # This loop uses the predefined sublists and shapes them into the
        #   specified shape. It removes the first n elements of self.tensor,
        #   combines them into a list of specified length, then adds that list
        #   on to the back of self.tensor
        while len(self.shape) > 1:
            size = self.shape.pop()
            length = prod(self.shape)

            for i in range(length):
                temp = []
                for j in range(size):
                    temp.append(self.tensor.pop(0)) # remove first element of
                                                    # tensor and save it in temp variable
                self.tensor.append(temp)

        print(self.tensor)


# Time and Space Complexity
#       For our analysis, N will represent the number of elements in the tensor
#   given by the shape parameter.
#
#       The first loop iterates through each element of the tensor once. The second
#   loop will iterate through the tensor once for every extra rank (from one to
#   n). Therefore, this process has a time complexity of:
#                                O(n^x)
#   where x is the rank of the given tensor.
#
#       This program uses the tensor to hold all values and only uses realtivley
#   small temporary values to create sublists. Therefore, this program has a
#   time compexity of:
#                               O(n)


# END CLASS DEFINITION ========================================================

data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2, 3, 2]

data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]

data2 = [0, 1, 2, 3, 4, 5]
shape2 = [8]

data3 = [0, 1, 2, 3, 4, 5, 4, 6, 12, 6, 1, 6, 6, 3, 7, 8, 21, 4]
shape3 = [2, 3, 5, 4, 3]


tensor0 = Tensor(data0, shape0)
tensor1 = Tensor(data1, shape1)
tensor2 = Tensor(data2, shape2)
#tensor3 = Tensor(data3, shape3) # WARNING: long output

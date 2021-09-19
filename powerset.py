import math;
 
class PowerSet:    
    
    def powerset(self,input_set):
     
    # set_size of power set of a set
    # with set_size n is (2**n -1)
        pow_input_set = (int) (math.pow(2, input_set));
        counter = 0;
        j = 0;
     
        for counter in range(0, pow_input_set):
            for j in range(0, input_set):
                if((counter & (1 << j)) > 0):
                    print(set[j], end = "");
            print("");
 
set = ['a', 'b', 'c'];
printPowerSet(set, 3);

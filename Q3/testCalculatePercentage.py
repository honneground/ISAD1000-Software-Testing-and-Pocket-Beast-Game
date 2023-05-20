"""
Question 3 A Equivalence Partitioning Basic Test Code Implementation
"""
import CalculatePercentage

def test_calculate_percentage():

    num1 = [1,2,1,0,-1]
    num2 = [2,1,-1,1,0]
    expRst = [50,-1,-1,-1,-1]
    msg = ["num2 > num1","num1 > num2","num1 ≤ 0","num2 ≤ 0","num1 ≤ 0, num2 ≤ 0"]    
    for i in range(len(msg)):
        assert abs(expRst[i] - CalculatePercentage.calculate_percentage(num1[i], num2[i]) < 0.000001), msg[i]

if __name__ == "__main__":
    test_calculate_percentage()
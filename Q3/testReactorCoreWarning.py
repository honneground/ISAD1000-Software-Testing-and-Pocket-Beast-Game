"""
Question 3 B BVA Basic Test Code Implementation
"""
import ReactorCoreWarning

def test_reactor_core_warning():
    inTemperatures = [299,300,649,650,799,800,949,950,1099,1100]
    expRst = ["Danger! Core temp too low","Warning! Core temp low. Decreased efficiency.","Warning! Core temp low. Decreased efficiency.","Reactor core operating at standard temperatures","Reactor core operating at standard temperatures","Reactor core operating at increased temperatures","Reactor core operating at increased temperatures","Warning! Core temp High. Deploy control rods.","Warning! Core temp High. Deploy control rods.","Danger! Core temp too high"]
    msg = ["too low / low lower boundary","too low / low upper boundary","low / standard lower boundary","low / standard upper boundary","standard / increased lower boundary","standard / increased upper boundary","increased / high lower boundary","increased / high upper boundary","high / dangerous lower boundary","high / dangerous upper boundary"]
    
    for i in range(len(msg)):
        assert expRst[i] == ReactorCoreWarning.reactor_core_warning(inTemperatures[i]), msg[i]

if __name__ == "__main__":
    test_reactor_core_warning()
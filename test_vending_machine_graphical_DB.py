# Dylan Brett (100933134)
# TPRG-2131-02
# Nov 17, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material
#
"""
For the 'vending_machine_graphical_DB.py' script - WORKS
"""

from vending_machine_graphical_DB import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # new machine object
    vending = VendingMachine()

    # Add the states
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())


    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'

    # test that the first coin causes a transition to 'coins'
    
    vending.event = '5'# a nicle
    vending.amount = 0 # set the amount back to zero after testing 5
    vending.go_to_state('waiting')
    vending.update() # update
    assert vending.state.name == 'add_coins'
    assert vending.amount == 5 # pennies, was .total
    
    vending.event = '10' # a dime
    vending.amount = 0 # set the amount back to zero after testing 10
    vending.go_to_state('waiting')
    vending.update() # update
    assert vending.state.name == 'add_coins'
    assert vending.amount == 10 # pennies, was .total
    
    vending.event = '25' # a quarter
    vending.amount = 0 # set the amount back to zero after testing 25
    vending.go_to_state('waiting')
    vending.update() # update
    assert vending.state.name == 'add_coins'
    assert vending.amount == 25 # pennies, was .total
    
    vending.event = '100' # a loonie
    vending.amount = 0 # set the amount back to zero after testing 100
    vending.go_to_state('waiting')
    vending.update() # update
    assert vending.state.name == 'add_coins'
    assert vending.amount == 100 # pennies, was .total
    
    vending.event = '200' # a twonie
    vending.amount = 0 # set the amount back to zero after testing 200
    vending.go_to_state('waiting')
    vending.update() # update
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200 # pennies, was .total
    
    

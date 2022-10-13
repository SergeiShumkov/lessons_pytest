from src.schemas.computer import Computer

from examples import computer

def test_computer():
    comp = Computer.parse_obj(computer)
    print(comp)
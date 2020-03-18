import pytest

# def func(x):
#     return x+1

# def test_answer():
#     assert func(3) == 6

class TestClass01:
    def test_one(self):
        x = 'this'
        assert 'h' in x
    
    def test_two(self):
        x = "hello"
        assert len(x)==5 
    @pytest.mark.faster
    def test_three(self):
        x = 'this'
        assert 's' in x
    @pytest.mark.slow
    def test_four(self):
        x = "hello"
        assert len(x)==7

# class TestClass02:
    
if  __name__== "__main__":
    pytest.main()
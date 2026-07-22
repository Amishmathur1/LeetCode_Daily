class Solution:
    def fizz_buzz_sequence(self, n):
        FIZZ = 'Fizz'
        BUZZ = 'Buzz'
        FIZZ_BUZZ = f'{FIZZ}{BUZZ}'
        is_multiple_of_three = n % 3 == 0 
        is_multiple_of_five = n % 5 == 0

        if is_multiple_of_three and is_multiple_of_five:
            return FIZZ_BUZZ

        if is_multiple_of_three:
            return FIZZ

        if is_multiple_of_five:
            return BUZZ

        return str(n)
		
    def fizzBuzz(self, n: int) -> List[str]:
        return list(self.fizz_buzz_sequence(i) for i in range(1, n + 1))
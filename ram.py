import psutil
import time
from pyfiglet import Figlet
from tqdm import tqdm

f=Figlet(font='slant')
print (f.renderText('Ram_info'))

for i in tqdm(range(100)):
     time.sleep(0.3)
def get_size(bytes,suffix='B'):
    factor = 1024
    for unit in ['','K','M','G','T','P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

#Get the swap memory details (if exists)
system = psutil.virtual_memory()
print (f'Total :{get_size(system.total)} ')
print (f'Available :{get_size(system.available)}')
print (f'Used :{get_size(system.used)}')
print (f'percentage :{system.percent}%')

swap = psutil.swap_memory()
print ('\nSwap pertition:')
print (f'Total: {get_size(swap.total)}')
print (f'Free: {get_size(swap.free)}')
print (f'Used: {get_size(swap.used)}')
print (f'Percentage: {swap.percent}%')

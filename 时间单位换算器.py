#时间单位转换器
a = int(input())

hours = a // 3600
a1 = a - hours*3600
minutes = a1 // 60
a2 = a1 - minutes*60
seconds = a - 3600*hours - 60*minutes

new_hours = str(hours)
new_minutes = str(minutes)
new_seconds = str(seconds)

print(f'{new_hours} 时 {new_minutes} 分 {new_seconds} 秒')
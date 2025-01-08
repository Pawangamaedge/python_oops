import asyncio as sn

def fun1(): # output will be: this is normal function
     print("this is normal function")

# this is coroutine function
async def syn_fun(): # output will be: coroutine object
     await sn.sleep(1)
     print("this is coroutine function")

async def syn_fun1():
     print("this is another coroutine function")



async def start_engine():
     print("engine starting....")
     await sn.sleep(2)
     print("engine started...")
     start_stop = str(input("""type "stop" to stop the engine: """))
     if start_stop == 'stop':
          await stop_engine()
     elif start_stop != 'stop':
          print("invalid command! Please try again")
     else:
          print("engine not stoped")

async def stop_engine():
     print("engine stoped...")

async def engine():
     print("welcome to engine master: ")
     await sn.sleep(1)
     eng = str(input("""type "start" to start the engine: """))
     if eng == 'start':
          await start_engine()
     elif eng != 'start':
          print("invalid command! Please try again")
     else: 
          print("engine game ended")



# fun1()
# sn.run(syn_fun())  # run() function allows us to run the async functions
# sn.run(syn_fun1())
# print(syn_fun1())  # output will be coroutine object
# sn.run(engine())




async def task_one():
    print("Task One starting...")
    await sn.sleep(2) 
    print("Task One completed!")

async def task_two():
    print("Task Two starting...")
    await sn.sleep(1)  
    print("Task Two completed!")

async def main():

    task1 = sn.create_task(task_one())
    task2 = sn.create_task(task_two())
    await task1
    await task2

# sn.run(main())


async def task_one():
    print("Task One starting...")
    await sn.sleep(2) 
    print("Task One completed!")

async def task_two():
    print("Task Two starting...")
    await sn.sleep(1)  
    print("Task Two completed!")

async def main():
     result = await sn.gather(task_one(), task_two())
     result
# sn.run(main())


async def time_out_fun():
     print("time function started")
     await sn.sleep(6)
     print("time function ended")

async def main():
     try:
          await sn.wait_for(time_out_fun(), timeout=5)
     except sn.TimeoutError:
          print("time out")

sn.run(main())
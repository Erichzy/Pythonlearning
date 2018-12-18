# 协程
- 历史历程
    - 3.4引入协程，用yield实现
    - 3.5引入协程语法
    - 实现的协程比较好的包有asyncio, tornado, gevent
- 定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序”。
- 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程的实现：
    - yield返回
    - send调用
 
- 协程的四个状态
    - inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime)
    - 代码案例v2
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
    - 止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
 
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
    - yield from从内部捕获StopIteration异常
    - 案例v03
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式出暂停，调用方可以直接把数据发给子生成器
        - 子生成器在把产出的值发给调用放
        - 子生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上
        - 案例v04
        - v05
        - 委派生成器
            - 包含 yield from 表达式的生成器函数
            - 委派生成器在 yield from 表达式处暂停时，调用方可以直接把数据发给子生成器。
            - 子生成器再把产出的值发给调用方。
            - 子生成器返回之后，解释器会抛出 StopIteration 异常，并把返回值附加到异常对象上，
        此时委派生成器会恢复。
            - v06
        
- # asyncio
- python3.4开始引入的标准库,内置了对移步io的支持
- asyncio本身是一个消息循环,
- 步骤
    - 创建消息循环
    - 把协程导入
    - 关闭
 - 案例08
 - 案例09-两个tasks
 - 案例v10-得到多个网站
 
# async and await
- 为了更好的表示异步io
- python3.5 开始引入
- 让coroutine代码更简洁
- 使用上,可以简单进行替换
    - 可以把 @asyncio.coroutine 替换成async
    - yield from 替换成await
- 案例v11, 把案例09直接替换
 
 
# aiohttp
- 介绍
    - asyncio实现单线程并发IO,在客户端用处不大
    - 在服务器端可以asyncio+coroutine配合,因为http是io操作
    - asyncio实现了TCP,UIDP,SSL等协议
    - aiohttp是给予asyncio实现的HTTP框架
    - pip install aiohttp
    - 案例07
    
    
# concurrent.futures
- python3新增的库
- 类似其他语言的线程池的概念
- 此模块利用multiprocessiong实现真正的平行计算
- 核心原理是：concurrent.futures会以子进程的形式，平行的运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。
由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个CPU内核。
- concurrent.futures.Executor 
    - ThreadPoolExecutor
    - ProcessPoolExecutor
- submit(fn, args, kwargs)
    - fn:异步执行的函数
    - args,kwargs:参数
    
             # 官方死锁案例
            import time
            def wait_on_b():
                time.sleep(5)
                print(b.result())  #b不会完成，他一直在等待a的return结果
                return 5

            def wait_on_a():
                time.sleep(5)
                print(a.result())  #同理a也不会完成，他也是在等待b的结果
                return 6


            executor = ThreadPoolExecutor(max_workers=2)
            a = executor.submit(wait_on_b)
            b = executor.submit(wait_on_a)
            
    - 案例v14
      
- map(fn, \*iterables, timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout: 超时时间
    - 案例 v12
    - 案例v15
    - 起执行结果是list,数据需要从list中取出来
    
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                print(list(executor.map(sleeper, x)))
           
- submit和map根据需要选一个即可
- 案例v13

- Future
    - 未来需要完成的任务
    - future 实例由Excutor.submit创建
    - 案例v17

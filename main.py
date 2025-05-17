RuntimeError                              Traceback (most recent call last)
<ipython-input-2-ce9dfdfd8074> in <cell line: 0>()
    131 
    132 print("Bot ready to prank! 😂")
--> 133 app.run()

2 frames
/usr/lib/python3.11/asyncio/base_events.py in _check_running(self)
    587     def _check_running(self):
    588         if self.is_running():
--> 589             raise RuntimeError('This event loop is already running')
    590         if events._get_running_loop() is not None:
    591             raise RuntimeError(

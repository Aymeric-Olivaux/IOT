#!/usr/bin/env python3

import asyncio
import time
from pixel_ring import pixel_ring
from gpiozero import LED


power = LED(5)


async def light_on():
    power.on()

    pixel_ring.set_brightness(20)
    pixel_ring.change_pattern('echo')
    pixel_ring.think()
    await asyncio.sleep(5)

    pixel_ring.off()
    power.off()

async def blink():
    power.on()

    pixel_ring.set_brightness(5)
    pixel_ring.change_pattern('googlehome')
    pixel_ring.wakeup()
    await asyncio.sleep(0.5)

    pixel_ring.off()
    power.off()

if __name__ == "__main__":
    asyncio.run(blink())
    time.sleep(4)
    asyncio.run(light_on())



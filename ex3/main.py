#! /usr/bin/env python

from clock import ClkDriver, Clock
from timer import Timer

from myhdl import Signal, toVHDL, traceSignals, Simulation, ResetSignal, toVerilog, intbv

if __name__ == "__main__":
    #ones_led = Signal(intbv(0)[7:])
    reset = ResetSignal(1, active=0, async=True)
    clk1us = Signal(bool(1))
    clk1ms = Signal(bool(0))
    clk500ms = Signal(bool(0))
    clk1s = Signal(bool(0))
    set_time = Signal(bool(1))
    set_hrs = Signal(bool(0))
    set_mins = Signal(bool(1))
    tim_secs1 = Signal(intbv(7, min=0, max=10))
    tim_secs10 = Signal(intbv(5, min=0, max=6))
    tim_mins1 = Signal(intbv(9, min=0, max=10))
    tim_mins10 = Signal(intbv(5, min=0, max=6))
    tim_hrs1 = Signal(intbv(3, min=0, max=10))
    tim_hrs10 = Signal(intbv(2, min=0, max=3))

    clkDriver = ClkDriver(clk1us)

    clock = Clock(clk1s, clk500ms, clk1ms, clk1us, reset)

    timblk = Timer(tim_secs1, tim_secs10, tim_mins1, tim_mins10, tim_hrs1, tim_hrs10, clk1s, clk500ms, set_time, set_hrs, set_mins, reset)

    sim = Simulation(clkDriver, clock, timblk)

    toVHDL(Clock, clk1s, clk500ms, clk1ms, clk1us, reset)
    toVHDL(Timer, tim_secs1, tim_secs10, tim_mins1, tim_mins10, tim_hrs1, tim_hrs10, clk1s, clk500ms, set_time, set_hrs, set_mins, reset)
    toVerilog(Timer, tim_secs1, tim_secs10, tim_mins1, tim_mins10, tim_hrs1, tim_hrs10, clk1s, clk500ms, set_time, set_hrs, set_mins, reset)
    toVerilog(Clock, clk1s, clk500ms, clk1ms, clk1us, reset)
    #traceSignals(Clock, clk1s, clk500ms, clk1ms, clk1us, reset)
    traceSignals(Timer, tim_secs1, tim_secs10, tim_mins1, tim_mins10, tim_hrs1, tim_hrs10, clk1s, clk500ms, set_time, set_hrs,
           set_mins, reset)
    sim.run(5 * 1000000*1000)
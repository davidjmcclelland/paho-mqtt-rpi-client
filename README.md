# TrueTwin Device Code

## Overview
This repository is part of the TrueTwin project that consists of several repositories.

The TrueTwin project is a proof-of-concept and spike to explore connecting a physical device to a virtual device (twin). The connection must allow either instance to publish changes so that it's twin syncs up in near-real-time.

This project is run on the physical device (Raspberry Pi). LightSwitch2.py handles turning an LED light on and off. lightStatus2.py is called to publish the status of the LED light each time it changes.

The Python code and this entire project is a fork of a starter project provided by HiveMQ. See [./README-HIVE_MQ.md](README-HIVE-MQ.md) for details.
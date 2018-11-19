# Mininet-Network-Emulator

Network emulation is a very useful tool, that allows us to test the performance and
evaluate behavior of networks, without having to physically build the network. Mininet is
a fast and reliable network emulator, and often described as one of the best open source
network emulators. The aim of this report is to give an overview of Mininet as a network
emulator and to give information on how the emulator's accuracy, scalability was tested.

To aid in testing of various networks, a Graphical User Interface (GUI) was developed.
This GUI would therefore allow any user to build custom, parameterized Mininet networks
quickly and easily. We will also take a brief look at how Mininet works and what it's
limitations are. 
We effectively tested Mininet's,
* bandwidth 
* delay
* packet loss
* jitter
consistency, to determine at which point measured values don't agree with theoretical
values and why the values don't agree. 

A further qualitative test was to stream actual video over the emulated network, to see how different network effects, affect a streamed video's quality. We then continued to connect Mininet hosts running on different hardware devices (Raspberry Pi's), by using Generic Routing Encapsulation (GRE) tunneling to connect the two Mininet networks - This was in essence a test of Mininet's scalability.

The same tests were performed, to ensure that Mininet's performance stays consistent
across both hardware and software interfaces. These tests helped us to draw insightful
performance graphs, which uncovered some of Mininet's strengths and limitations.

A final test was to build a physical network, consisting of real hosts and switches. The
GUI was then used to build a replica of this network, under the same network conditions,
in Mininet. Testing whether the emulated network performs the same as the physical
network, would prove that Mininet is an accurate and effcient emulator.

From test results we were able to conclude that Mininet is an accurate and scalable
network emulator. However, Mininet's performance relies heavily on the host device's
available resources. Following an in-depth discussion of test results, contributions of this
project, some recommendations and examples of further work will be given and discussed.

Skripsie Project 2016 - IT de Villiers

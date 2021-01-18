ip netns add h1
ip netns add h2
ip netns add h3
ip netns add h4
ovs-vsctl add-br s1
ip link add s1-eth1 type veth peer name h1-eth0
ip link add s1-eth2 type veth peer name h2-eth0
ip link add s1-eth3 type veth peer name h3-eth0
ip link add s1-eth4 type veth peer name h4-eth0
ip link set h1-eth0 netns h1
ip link set h2-eth0 netns h2
ip link set h3-eth0 netns h3
ip link set h4-eth0 netns h4
ovs-vsctl add-port s1 s1-eth1
ovs-vsctl add-port s1 s1-eth2
ovs-vsctl add-port s1 s1-eth3
ovs-vsctl add-port s1 s1-eth4
ip netns exec h1 ifconfig h1-eth0 10.0.1.1 up
ip netns exec h2 ifconfig h2-eth0 10.0.2.1 up
ip netns exec h3 ifconfig h3-eth0 10.0.3.1 up
ip netns exec h4 ifconfig h4-eth0 10.0.4.1 up
ip addr add 10.0.1.2/24 dev s1-eth1
ip addr add 10.0.2.2/24 dev s1-eth2
ip addr add 10.0.3.2/24 dev s1-eth3
ip addr add 10.0.4.2/24 dev s1-eth4
ip link set s1-eth1 up
ip link set s1-eth2 up
ip link set s1-eth3 up
ip link set s1-eth4 up
ip netns exec h1 ip link set lo up
ip netns exec h2 ip link set lo up
ip netns exec h3 ip link set lo up
ip netns exec h4 ip link set lo up
ip netns exec h1 ip route add default via 10.0.1.2
ip netns exec h2 ip route add default via 10.0.2.2
ip netns exec h3 ip route add default via 10.0.3.2
ip netns exec h4 ip route add default via 10.0.4.2

ip netns exec h1 ping 10.0.2.1

"""
Scalable Distributed Systems
============================
SeqNumber Generator
===================
Share screen to zoom meeting.


SeqNumber Generator (one counter: 256bit)
- increment
- skip is ok
- 1000 years


client1: 1,3,7,19,9199
client2:   2,4,6,10,10k,20k,30k
client3:   11,111,1111,111111
client4:  22,222,22222,2222222

//[..............................]
/


1. Option: using DBMS
   Performance issue only one client can write.

2. OPtion2 : Using multiple DBMS.

   hash(cliedid)%mod --> DBMS

   client 1 -const_hash--> dbms[j] ---> (R[j], 71)
   client 1 -const_hash--> dbms[j] ---> (R[j], 171)
   client 1 -const_hash--> dbms[j] ---> (R[j], 271)
   client 1 -const_hash--> dbms[j] ---> (R[j], 371)
   client 1 -const_hash--> dbms[j] ---> (R[j], 471)

   dbms[j] dead
   dbms[j']  continue to finish j's job

      j --> j' (how long?)

        primary --->failover --->secondary
           latency 1 second

                    failover latency
                    lb check healthy or not?
                    if primary is healthy
                        switch map "END_POINT" to secondary

        3 db died
        ========

           client 1: retry 10 second....



        x=5.............sync..........x=5
            replication latency=?  500ms
            same region latency = ?
            remote region latency = ?


                      ms?  second?

    1 billion clients.  10 requets per second per client
    10 Billion requests per second
    10B/10M = 1K DBMS  (3K DBMS)

      1. Throughput (RPS) 10 QPS
      2. Response Time.
      3. Hot Spot.

     one machine:
     __sync_fetch_and_add(&x, 1); //atomic_inc
     // how many ns?  100ns   10M requests per second
     // 100Gbps network:  10GB/s  10GB/packet_size=
          10GB/1KB = 10M requests per second

     SSD.write? How fast?

     1000 -> 1001

     1000
     1001
     1002

      10M requests per second
      ==>

      DDR: 40GB/s  (memory)
         0.2 ms (memory)

      SSD: 4GB/s (NVMe-PCIe SSD: 16 channel run in parallel)
       PCIe line ==> [0...15]

           4GB/4KB page size = 1M writes per second
           100* 10*K writes per second
           0.1ms write latency
           1ms latency for SSD.

      HDD: 400MB/s
      Net:  1GB, 10GB/s

     __sync_fetch_and_add(&x, 1); //atomic_inc
     100ns

     1ns  1GHz, x++; 1ns
     load/store: memory:
     1000ns

     100*10^-9 = 10^-7
     10^4  ==> 1ms ==> 10K line assembly code operations.
     1ms = 10^-3
     1 ms( CPU) 2 ms(memory) 10 ms (Disk)  100 QPS.

     100 requests per second





     restAPI getNextNumber() request package size?
         how many bytes? L2 l3 l4  [256 bits]


 OPtion 3: precalculate DBMS.
         1K DBMS: 10B/sec  -->
         10B*100K second /day =  1000TB; 1PB

         1K ...1TB cache = 1PB good for 1 day


         __sync_fetch_and_add(&x, 1); 100ns
                                  1ns cpu

                                  1000ns DDR load memory
                                  1000 thread:
                                     1ns

       1B*4Bytes = 4GB data. L2 cache 4GB

        1) generate 4Billion number saved in L2 cache.

      init() {

          l2_cache_mem[] = read 4GB ==> L2 cache
              //1 seocnds
          counter = ssd.read_counter() + 10 billions;
          i = 0;

      }//10 second reboot.

      Number getNext() {

          if (i == 1billion) {
             counter++;
             ssd.write(counter);
             i = 0;
          }
          Clear

       cnt = (counter << 32) +
               l2_cache_mem[thread_id][i++];




          return cnt;

      }

             sup_root // 10K per second seqNumber
             ///n1. store.

             10 seconds.

             /\\\\\\\\\\\
             1K per seconds.
             1 per 1ms
            root           .....  root (10 data centers)
            /\\\\\                            //\\\\
       cache server [4GB l2 cache].....1k

            1k*1= 10K cache servers.



            cache_server: 10M request seconds. (network throughput)
            10m*10K = 100 billion requests per second


            cache: return sup_root.n1 <<128
                           ---------- 10 seconds

            +              root.n2 << 64
            +             l2_mem_cache[threadID][local_i++];

            sup_root, root, cache]

            [n1       n2,    n3]
            ***       ---  ----
            ^^^
            (n1<<128) + [(n2<<64) + (n3)]
            ^^^^
            state saved in RDMS
             --
             &

            dbms[j] dead
   dbms[j']  continue to finish j's job
"""
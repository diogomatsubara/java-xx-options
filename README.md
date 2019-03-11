This repo is a documentation repository for the many -XX Java JVM options.

The list came from: http://stas-blogspot.blogspot.com/2011/07/most-complete-list-of-xx-options-for.html

All I did was to format it to markdown. And having it here and not in someone's blogpost also makes it easier to update and keep it up to date.

| Name | Description | Default | Type |
| --- | --- | --- | --- |
| PRODUCT | | | |
| UseMembar | (Unstable) Issues membars on thread state transitions | false | bool |
| UnlockCommercialFeatures | Enables Oracle Java SE users to control when licensed features are allowed to run. Since Java SE 7 Update 4. | false | bool |
| PrintCommandLineFlags | Prints flags that appeared on the command line | false | bool |
| UseGCLogFileRotation | Prevent large gclog file for long running app. Requires -Xloggc:<filename>. Since Java7. | false | bool |
| NumberOfGCLogFiles | Number of gclog files in rotation. Default: 0, no rotation. Only valid with UseGCLogFileRotation. Since Java7. | 0 | uintx |
| GCLogFileSize | GC log file size, Default: 0 bytes, no rotation. Only valid with UseGCLogFileRotation. Since Java7. | 0 | uintx |
| JavaMonitorsInStackTrace | Print info. about Java monitor locks when the stacks are dumped | true | bool |
| LargePageSizeInBytes | Large page size (0 to let VM choose the page size | 0 | uintx |
| LargePageHeapSizeThreshold | Use large pages if max heap is at least this big | 128*M | uintx |
| ForceTimeHighResolution | Using high time resolution(For Win32 only) | false | bool |
| PrintVMQWaitTime | Prints out the waiting time in VM operation queue | false | bool |
| PrintJNIResolving | Used to implement -v:jni | false | bool |
| UseInlineCaches | Use Inline Caches for virtual calls | true | bool |
| UseCompilerSafepoints | Stop at safepoints in compiled code | true | bool |
| UseSplitVerifier | use split verifier with StackMapTable attributes | true | bool |
| FailOverToOldVerifier | fail over to old verifier when split verifier fails | true | bool |
| SuspendRetryCount | Maximum retry count for an external suspend request | 50 | intx |
| SuspendRetryDelay | Milliseconds to delay per retry (* current_retry_count) | 5 | intx |
| UseSuspendResumeThreadLists | Enable SuspendThreadList and ResumeThreadList | true | bool |
| MaxFDLimit | Bump the number of file descriptors to max in solaris. | true | bool |
| BytecodeVerificationRemote | Enables the Java bytecode verifier for remote classes | true | bool |
| BytecodeVerificationLocal | Enables the Java bytecode verifier for local classes | false | bool |
| PrintGCApplicationConcurrentTime | Print the time the application has been running | false | bool |
| PrintGCApplicationStoppedTime | Print the time the application has been stopped | false | bool |
| ShowMessageBoxOnError | Keep process alive on VM fatal error | false | bool |
| SuppressFatalErrorMessage | Do NO Fatal Error report [Avoid deadlock] | false | bool |
| OnError | Run user-defined commands on fatal error; see VMError.cpp for examples | "" | ccstr |
| OnOutOfMemoryError | Run user-defined commands on first java.lang.OutOfMemoryError | "" | ccstr |
| PrintCompilation | Print compilations | false | bool |
| StackTraceInThrowable | Collect backtrace in throwable when exception happens | true | bool |
| OmitStackTraceInFastThrow | Omit backtraces for some 'hot' exceptions in optimized code | true | bool |
| ProfilerPrintByteCodeStatistics | Prints byte code statictics when dumping profiler output | false | bool |
| ProfilerRecordPC | Collects tick for each 16 byte interval of compiled code | false | bool |
| UseNUMA | Enables NUMA support. See details here | false | bool |
| ProfileVM | Profiles ticks that fall within VM (either in the VM Thread or VM code called through stubs) | false | bool |
| ProfileIntervals | Prints profiles for each interval (see ProfileIntervalsTicks) | false | bool |
| RegisterFinalizersAtInit | Register finalizable objects at end of Object. or after allocation. | true | bool |
| ClassUnloading | Do unloading of classes | true | bool |
| ConvertYieldToSleep | Converts yield to a sleep of MinSleepInterval to simulate Win32 behavior (SOLARIS only) | false | bool |
| UseBoundThreads | Bind user level threads to kernel threads (for SOLARIS only) | true | bool |
| UseLWPSynchronization | Use LWP-based instead of libthread-based synchronization (SPARC only) | true | bool |
| SyncKnobs | (Unstable) Various monitor synchronization tunables | "" | ccstr |
| EmitSync | (Unsafe,Unstable) Controls emission of inline sync fast-path code | 0 | intx |
| AlwaysInflate | (Unstable) Force inflation | 0 | intx |
| Atomics | (Unsafe,Unstable) Diagnostic - Controls emission of atomics | 0 | intx |
| EmitLFence | (Unsafe,Unstable) Experimental | 0 | intx |
| AppendRatio | (Unstable) Monitor queue fairness" ) product(intx, SyncFlags, 0,(Unsafe,Unstable) Experimental Sync flags" ) product(intx, SyncVerbose, 0,(Unstable)" ) product(intx, ClearFPUAtPark, 0,(Unsafe,Unstable)" ) product(intx, hashCode, 0, (Unstable) select hashCode generation algorithm" ) product(intx, WorkAroundNPTLTimedWaitHang, 1, (Unstable, Linux-specific)" avoid NPTL-FUTEX hang pthread_cond_timedwait" ) product(bool, FilterSpuriousWakeups , true, Prevent spurious or premature wakeups from object.wait" (Solaris only) | 11 | intx |
| AdjustConcurrency | call thr_setconcurrency at thread create time to avoid LWP starvation on MP systems (For Solaris Only) | false | bool |
| ReduceSignalUsage | Reduce the use of OS signals in Java and/or the VM | false | bool |
| AllowUserSignalHandlers | Do not complain if the application installs signal handlers (Solaris & Linux only) | false | bool |
| UseSignalChaining | Use signal-chaining to invoke signal handlers installed by the application (Solaris & Linux only) | true | bool |
| UseAltSigs | Use alternate signals instead of SIGUSR1 & SIGUSR2 for VM internal signals. (Solaris only) | false | bool |
| UseSpinning | Use spinning in monitor inflation and before entry | false | bool |
| PreSpinYield | Yield before inner spinning loop | false | bool |
| PostSpinYield | Yield after inner spinning loop | true | bool |
| UsePopCountInstruction | Where possible replaces call to Integer.bitCount() with assembly instruction, i.e. POCCNT on Intel, POPC on Sparc, etc | true | bool |
| AllowJNIEnvProxy | Allow JNIEnv proxies for jdbx | false | bool |
| JNIDetachReleasesMonitors | JNI DetachCurrentThread releases monitors owned by thread | true | bool |
| RestoreMXCSROnJNICalls | Restore MXCSR when returning from JNI calls | false | bool |
| CheckJNICalls | Verify all arguments to JNI calls | false | bool |
| UseFastJNIAccessors | Use optimized versions of GetField | true | bool |
| EagerXrunInit | Eagerly initialize -Xrun libraries; allows startup profiling, but not all -Xrun libraries may support the state of the VM at this time | false | bool |
| PreserveAllAnnotations | Preserve RuntimeInvisibleAnnotations as well as RuntimeVisibleAnnotations | false | bool |
| LazyBootClassLoader | Enable/disable lazy opening of boot class path entries | true | bool |
| UseBiasedLocking | Enable biased locking in JVM | true | bool |
| BiasedLockingStartupDelay | Number of milliseconds to wait before enabling biased locking | 4000 | intx |
| BiasedLockingBulkRebiasThreshold | Threshold of number of revocations per type to try to rebias all objects in the heap of that type | 20 | intx |
| BiasedLockingBulkRevokeThreshold | Threshold of number of revocations per type to permanently revoke biases of all objects in the heap of that type | 40 | intx |
| BiasedLockingDecayTime | Decay time (in milliseconds) to re-enable bulk rebiasing of a type after previous bulk rebias | 25000 | intx |
| TraceJVMTI | Trace flags for JVMTI functions and events | "" | ccstr |
| StressLdcRewrite | Force ldc -> ldc_w rewrite during RedefineClasses | false | bool |
| TraceRedefineClasses | Trace level for JVMTI RedefineClasses | 0 | intx |
| VerifyMergedCPBytecodes | Verify bytecodes after RedefineClasses constant pool merging | true | bool |
| HPILibPath | Specify alternate path to HPI library | "" | ccstr |
| TraceClassResolution | Trace all constant pool resolutions (for debugging) | false | bool |
| TraceBiasedLocking | Trace biased locking in JVM | false | bool |
| TraceMonitorInflation | Trace monitor inflation in JVM | false | bool |
| Use486InstrsOnly | Use 80486 Compliant instruction subset | false | bool |
| UseSerialGC | Tells whether the VM should use serial garbage collector | false | bool |
| UseParallelGC | Use parallel garbage collection for scavenges. (Introduced in 1.4.1) | true | bool |
| UseParallelOldGC | Use parallel garbage collection for the full collections. Enabling this option automatically sets -XX:+UseParallelGC. (Introduced in 5.0 update 6) | 'false' before Java 7 update 4 and 'true' after that version | bool |
| UseParallelOldGCCompacting | In the Parallel Old garbage collector use parallel compaction | true | bool |
| UseParallelDensePrefixUpdate | In the Parallel Old garbage collector use parallel dense" prefix update | true | bool |
| HeapMaximumCompactionInterval | How often should we maximally compact the heap (not allowing any dead space) | 20 | uintx |
| HeapFirstMaximumCompactionCount | The collection count for the first maximum compaction | 3 | uintx |
| UseMaximumCompactionOnSystemGC | In the Parallel Old garbage collector maximum compaction for a system GC | true | bool |
| ParallelOldDeadWoodLimiterMean | The mean used by the par compact dead wood" limiter (a number between 0-100). | 50 | uintx |
| ParallelOldDeadWoodLimiterStdDev | The standard deviation used by the par compact dead wood" limiter (a number between 0-100). | 80 | uintx |
| UseParallelOldGCDensePrefix | Use a dense prefix with the Parallel Old garbage collector | true | bool |
| ParallelGCThreads | Number of parallel threads parallel gc will use | 0 | uintx |
| ParallelCMSThreads | Max number of threads CMS will use for concurrent work | 0 | uintx |
| YoungPLABSize | Size of young gen promotion labs (in HeapWords) | 4096 | uintx |
| OldPLABSize | Size of old gen promotion labs (in HeapWords).  See good explanation about that parameter here. | 1024 | uintx |
| GCTaskTimeStampEntries | Number of time stamp entries per gc worker thread | 200 | uintx |
| AlwaysTenure | Always tenure objects in eden. (ParallelGC only) | false | bool |
| NeverTenure | Never tenure objects in eden, May tenure on overflow" (ParallelGC only) | false | bool |
| ScavengeBeforeFullGC | Scavenge youngest generation before each full GC," used with UseParallelGC | true | bool |
| UseCompressedOops | Enables object-reference compression capabilities via the Compressed References. Have sense just on 64bit JVM. See more details here. | false | bool |
| UseConcMarkSweepGC | Use Concurrent Mark-Sweep GC in the old generation | false | bool |
| ExplicitGCInvokesConcurrent | A System.gc() request invokes a concurrent collection;" (effective only when UseConcMarkSweepGC) | false | bool |
| UseCMSBestFit | Use CMS best fit allocation strategy | true | bool |
| UseCMSCollectionPassing | Use passing of collection from background to foreground | true | bool |
| UseParNewGC | Use parallel threads in the new generation. | false | bool |
| ParallelGCVerbose | Verbose output for parallel GC. | false | bool |
| ParallelGCBufferWastePct | wasted fraction of parallel allocation buffer. | 10 | intx |
| ParallelGCRetainPLAB | Retain parallel allocation buffers across scavenges. | true | bool |
| TargetPLABWastePct | target wasted space in last buffer as pct of overall allocation | 10 | intx |
| PLABWeight | Percentage (0-100) used to weight the current sample when" computing exponentially decaying average for ResizePLAB. | 75 | uintx |
| ResizePLAB | Dynamically resize (survivor space) promotion labs | true | bool |
| PrintPLAB | Print (survivor space) promotion labs sizing decisions | false | bool |
| ParGCArrayScanChunk | Scan a subset and push remainder, if array is bigger than this | 50 | intx |
| ParGCDesiredObjsFromOverflowList | The desired number of objects to claim from the overflow list | 20 | intx |
| CMSParPromoteBlocksToClaim | Number of blocks to attempt to claim when refilling CMS LAB for parallel GC. | 50 | uintx |
| AlwaysPreTouch | It forces all freshly committed pages to be pre-touched. | false | bool |
| CMSUseOldDefaults | A flag temporarily introduced to allow reverting to some older" default settings; older as of 6.0 | false | bool |
| CMSYoungGenPerWorker | The amount of young gen chosen by default per GC worker thread available | 16*M | intx |
| CMSIncrementalMode | Whether CMS GC should operate in \"incremental\" mode | false | bool |
| CMSIncrementalDutyCycle | CMS incremental mode duty cycle (a percentage, 0-100). If" CMSIncrementalPacing is enabled, then this is just the initial" value | 10 | uintx |
| CMSIncrementalPacing | Whether the CMS incremental mode duty cycle should be automatically adjusted | true | bool |
| CMSIncrementalDutyCycleMin | Lower bound on the duty cycle when CMSIncrementalPacing is" enabled (a percentage, 0-100). | 0 | uintx |
| CMSIncrementalSafetyFactor | Percentage (0-100) used to add conservatism when computing the" duty cycle. | 10 | uintx |
| CMSIncrementalOffset | Percentage (0-100) by which the CMS incremental mode duty cycle" is shifted to the right within the period between young GCs | 0 | uintx |
| CMSExpAvgFactor | Percentage (0-100) used to weight the current sample when" computing exponential averages for CMS statistics. | 25 | uintx |
| CMS_FLSWeight | Percentage (0-100) used to weight the current sample when" computing exponentially decating averages for CMS FLS statistics. | 50 | uintx |
| CMS_FLSPadding | The multiple of deviation from mean to use for buffering" against volatility in free list demand. | 2 | uintx |
| FLSCoalescePolicy | CMS: Aggression level for coalescing, increasing from 0 to 4 | 2 | uintx |
| CMS_SweepWeight | Percentage (0-100) used to weight the current sample when" computing exponentially decaying average for inter-sweep duration. | 50 | uintx |
| CMS_SweepPadding | The multiple of deviation from mean to use for buffering" against volatility in inter-sweep duration. | 2 | uintx |
| CMS_SweepTimerThresholdMillis | Skip block flux-rate sampling for an epoch unless inter-sweep duration exceeds this threhold in milliseconds | 10 | uintx |
| CMSClassUnloadingEnabled | Whether class unloading enabled when using CMS GC | false | bool |
| CMSCompactWhenClearAllSoftRefs | Compact when asked to collect CMS gen with clear_all_soft_refs | true | bool |
| UseCMSCompactAtFullCollection | Use mark sweep compact at full collections | true | bool |
| CMSFullGCsBeforeCompaction | Number of CMS full collection done before compaction if > 0 | 0 | uintx |
| CMSIndexedFreeListReplenish | Replenish and indexed free list with this number of chunks | 4 | uintx |
| CMSLoopWarn | Warn in case of excessive CMS looping | false | bool |
| CMSMarkStackSize | Size of CMS marking stack | 32*K | uintx |
| CMSMarkStackSizeMax | Max size of CMS marking stack | 4*M | uintx |
| CMSMaxAbortablePrecleanLoops | (Temporary, subject to experimentation)" Maximum number of abortable preclean iterations, if > 0 | 0 | uintx |
| CMSMaxAbortablePrecleanTime | (Temporary, subject to experimentation)" Maximum time in abortable preclean in ms | 5000 | intx |
| CMSAbortablePrecleanMinWorkPerIteration | (Temporary, subject to experimentation)" Nominal minimum work per abortable preclean iteration | 100 | uintx |
| CMSAbortablePrecleanWaitMillis | (Temporary, subject to experimentation)" Time that we sleep between iterations when not given" enough work per iteration | 100 | intx |
| CMSRescanMultiple | Size (in cards) of CMS parallel rescan task | 32 | uintx |
| CMSConcMarkMultiple | Size (in cards) of CMS concurrent MT marking task | 32 | uintx |
| CMSRevisitStackSize | Size of CMS KlassKlass revisit stack | 1*M | uintx |
| CMSAbortSemantics | Whether abort-on-overflow semantics is implemented | false | bool |
| CMSParallelRemarkEnabled | Whether parallel remark enabled (only if ParNewGC) | true | bool |
| CMSParallelSurvivorRemarkEnabled | Whether parallel remark of survivor space" enabled (effective only if CMSParallelRemarkEnabled) | true | bool |
| CMSPLABRecordAlways | Whether to always record survivor space PLAB bdries" (effective only if CMSParallelSurvivorRemarkEnabled) | true | bool |
| CMSConcurrentMTEnabled | Whether multi-threaded concurrent work enabled (if ParNewGC) | true | bool |
| CMSPermGenPrecleaningEnabled | Whether concurrent precleaning enabled in perm gen" (effective only when CMSPrecleaningEnabled is true) | true | bool |
| CMSPermGenSweepingEnabled | Whether sweeping of perm gen is enabled | false | bool |
| CMSPrecleaningEnabled | Whether concurrent precleaning enabled | true | bool |
| CMSPrecleanIter | Maximum number of precleaning iteration passes | 3 | uintx |
| CMSPrecleanNumerator | CMSPrecleanNumerator:CMSPrecleanDenominator yields convergence" ratio | 2 | uintx |
| CMSPrecleanDenominator | CMSPrecleanNumerator:CMSPrecleanDenominator yields convergence" ratio | 3 | uintx |
| CMSPrecleanRefLists1 | Preclean ref lists during (initial) preclean phase | true | bool |
| CMSPrecleanRefLists2 | Preclean ref lists during abortable preclean phase | false | bool |
| CMSPrecleanSurvivors1 | Preclean survivors during (initial) preclean phase | false | bool |
| CMSPrecleanSurvivors2 | Preclean survivors during abortable preclean phase | true | bool |
| CMSPrecleanThreshold | Don't re-iterate if #dirty cards less than this | 1000 | uintx |
| CMSCleanOnEnter | Clean-on-enter optimization for reducing number of dirty cards | true | bool |
| CMSRemarkVerifyVariant | Choose variant (1,2) of verification following remark | 1 | uintx |
| CMSScheduleRemarkEdenSizeThreshold | If Eden used is below this value, don't try to schedule remark | 2*M | uintx |
| CMSScheduleRemarkEdenPenetration | The Eden occupancy % at which to try and schedule remark pause | 50 | uintx |
| CMSScheduleRemarkSamplingRatio | Start sampling Eden top at least before yg occupancy reaches" 1/ of the size at which we plan to schedule remark | 5 | uintx |
| CMSSamplingGrain | The minimum distance between eden samples for CMS (see above) | 16*K | uintx |
| CMSScavengeBeforeRemark | Attempt scavenge before the CMS remark step | false | bool |
| CMSWorkQueueDrainThreshold | Don't drain below this size per parallel worker/thief | 10 | uintx |
| CMSWaitDuration | Time in milliseconds that CMS thread waits for young GC | 2000 | intx |
| CMSYield | Yield between steps of concurrent mark & sweep | true | bool |
| CMSBitMapYieldQuantum | Bitmap operations should process at most this many bits" between yields | 10*M | uintx |
| BlockOffsetArrayUseUnallocatedBlock | Maintain _unallocated_block in BlockOffsetArray" (currently applicable only to CMS collector) | trueInDebug | bool |
| RefDiscoveryPolicy | Whether reference-based(0) or referent-based(1) | 0 | intx |
| ParallelRefProcEnabled | Enable parallel reference processing whenever possible | false | bool |
| CMSTriggerRatio | Percentage of MinHeapFreeRatio in CMS generation that is allocated before a CMS collection cycle commences | 80 | intx |
| CMSBootstrapOccupancy | Percentage CMS generation occupancy at which to initiate CMS collection for bootstrapping collection stats | 50 | intx |
| CMSInitiatingOccupancyFraction | Percentage CMS generation occupancy to start a CMS collection cycle (A negative value means that CMSTirggerRatio is used). See good explanation about that parameter here. | -1 | intx |
| UseCMSInitiatingOccupancyOnly | Only use occupancy as a crierion for starting a CMS collection.  See good explanation about that parameter here. | false | bool |
| HandlePromotionFailure | The youngest generation collection does not require" a guarantee of full promotion of all live objects. | true | bool |
| PreserveMarkStackSize | Size for stack used in promotion failure handling | 40 | uintx |
| ZeroTLAB | Zero out the newly created TLAB | false | bool |
| PrintTLAB | Print various TLAB related information | false | bool |
| TLABStats | Print various TLAB related information | true | bool |
| AlwaysActAsServerClassMachine | Always act like a server-class machine | false | bool |
| DefaultMaxRAM | Maximum real memory size for setting server class heap size | G | uintx |
| DefaultMaxRAMFraction | Fraction (1/n) of real memory used for server class max heap | 4 | uintx |
| DefaultInitialRAMFraction | Fraction (1/n) of real memory used for server class initial heap | 64 | uintx |
| UseAutoGCSelectPolicy | Use automatic collection selection policy | false | bool |
| AutoGCSelectPauseMillis | Automatic GC selection pause threshhold in ms | 5000 | uintx |
| UseAdaptiveSizePolicy | Use adaptive generation sizing policies | true | bool |
| UsePSAdaptiveSurvivorSizePolicy | Use adaptive survivor sizing policies | true | bool |
| UseAdaptiveGenerationSizePolicyAtMinorCollection | Use adaptive young-old sizing policies at minor collections | true | bool |
| UseAdaptiveGenerationSizePolicyAtMajorCollection | Use adaptive young-old sizing policies at major collections | true | bool |
| UseAdaptiveSizePolicyWithSystemGC | Use statistics from System.GC for adaptive size policy | false | bool |
| UseAdaptiveGCBoundary | Allow young-old boundary to move | false | bool |
| AdaptiveSizeThroughPutPolicy | Policy for changeing generation size for throughput goals | 0 | uintx |
| AdaptiveSizePausePolicy | Policy for changing generation size for pause goals | 0 | uintx |
| AdaptiveSizePolicyInitializingSteps | Number of steps where heuristics is used before data is used | 20 | uintx |
| AdaptiveSizePolicyOutputInterval | Collecton interval for printing information, zero => never | 0 | uintx |
| UseAdaptiveSizePolicyFootprintGoal | Use adaptive minimum footprint as a goal | true | bool |
| AdaptiveSizePolicyWeight | Weight given to exponential resizing, between 0 and 100 | 10 | uintx |
| AdaptiveTimeWeight | Weight given to time in adaptive policy, between 0 and 100 | 25 | uintx |
| PausePadding | How much buffer to keep for pause time | 1 | uintx |
| PromotedPadding | How much buffer to keep for promotion failure | 3 | uintx |
| SurvivorPadding | How much buffer to keep for survivor overflow | 3 | uintx |
| AdaptivePermSizeWeight | Weight for perm gen exponential resizing, between 0 and 100 | 20 | uintx |
| PermGenPadding | How much buffer to keep for perm gen sizing | 3 | uintx |
| ThresholdTolerance | Allowed collection cost difference between generations | 10 | uintx |
| AdaptiveSizePolicyCollectionCostMargin | If collection costs are within margin, reduce both by full delta | 50 | uintx |
| YoungGenerationSizeIncrement | Adaptive size percentage change in young generation | 20 | uintx |
| YoungGenerationSizeSupplement | Supplement to YoungedGenerationSizeIncrement used at startup | 80 | uintx |
| YoungGenerationSizeSupplementDecay | Decay factor to YoungedGenerationSizeSupplement | 8 | uintx |
| TenuredGenerationSizeIncrement | Adaptive size percentage change in tenured generation | 20 | uintx |
| TenuredGenerationSizeSupplement | Supplement to TenuredGenerationSizeIncrement used at startup | 80 | uintx |
| TenuredGenerationSizeSupplementDecay | Decay factor to TenuredGenerationSizeIncrement | 2 | uintx |
| MaxGCPauseMillis | Adaptive size policy maximum GC pause time goal in msec | max_uintx | uintx |
| MaxGCMinorPauseMillis | Adaptive size policy maximum GC minor pause time goal in msec | max_uintx | uintx |
| GCTimeRatio | Adaptive size policy application time to GC time ratio | 99 | uintx |
| AdaptiveSizeDecrementScaleFactor | Adaptive size scale down factor for shrinking | 4 | uintx |
| UseAdaptiveSizeDecayMajorGCCost | Adaptive size decays the major cost for long major intervals | true | bool |
| AdaptiveSizeMajorGCDecayTimeScale | Time scale over which major costs decay | 10 | uintx |
| MinSurvivorRatio | Minimum ratio of young generation/survivor space size | 3 | uintx |
| InitialSurvivorRatio | Initial ratio of eden/survivor space size | 8 | uintx |
| BaseFootPrintEstimate | Estimate of footprint other than Java Heap | 256*M | uintx |
| UseGCOverheadLimit | Use policy to limit of proportion of time spent in GC before an OutOfMemory error is thrown | true | bool |
| GCTimeLimit | Limit of proportion of time spent in GC before an OutOfMemory" error is thrown (used with GCHeapFreeLimit) | 98 | uintx |
| GCHeapFreeLimit | Minimum percentage of free space after a full GC before an OutOfMemoryError is thrown (used with GCTimeLimit) | 2 | uintx |
| PrintAdaptiveSizePolicy | Print information about AdaptiveSizePolicy | false | bool |
| DisableExplicitGC | Tells whether calling System.gc() does a full GC | false | bool |
| CollectGen0First | Collect youngest generation before each full GC | false | bool |
| BindGCTaskThreadsToCPUs | Bind GCTaskThreads to CPUs if possible | false | bool |
| UseGCTaskAffinity | Use worker affinity when asking for GCTasks | false | bool |
| ProcessDistributionStride | Stride through processors when distributing processes | 4 | uintx |
| CMSCoordinatorYieldSleepCount | number of times the coordinator GC thread will sleep while yielding before giving up and resuming GC | 10 | uintx |
| CMSYieldSleepCount | number of times a GC thread (minus the coordinator) will sleep while yielding before giving up and resuming GC | 0 | uintx |
| PrintGCTaskTimeStamps | Print timestamps for individual gc worker thread tasks | false | bool |
| TraceClassLoadingPreorder | Trace all classes loaded in order referenced (not loaded) | false | bool |
| TraceGen0Time | Trace accumulated time for Gen 0 collection | false | bool |
| TraceGen1Time | Trace accumulated time for Gen 1 collection | false | bool |
| PrintTenuringDistribution | Print tenuring age information | false | bool |
| PrintHeapAtSIGBREAK | Print heap layout in response to SIGBREAK | true | bool |
| TraceParallelOldGCTasks | Trace multithreaded GC activity | false | bool |
| PrintParallelOldGCPhaseTimes | Print the time taken by each parallel old gc phase." PrintGCDetails must also be enabled. | false | bool |
| CITime | collect timing information for compilation | false | bool |
| Inline | enable inlining | true | bool |
| ClipInlining | clip inlining if aggregate method exceeds DesiredMethodLimit | true | bool |
| UseTypeProfile | Check interpreter profile for historically monomorphic calls | true | bool |
| TypeProfileMinimumRatio | Minimum ratio of profiled majority type to all minority types | 9 | intx |
| Tier1UpdateMethodData | Update methodDataOops in Tier1-generated code | false | bool |
| PrintVMOptions | print VM flag settings | trueInDebug | bool |
| ErrorFile | If an error occurs, save the error data to this file [default: ./hs_err_pid%p.log] (%p replaced with pid) | "" | ccstr |
| DisplayVMOutputToStderr | If DisplayVMOutput is true, display all VM output to stderr | false | bool |
| DisplayVMOutputToStdout | If DisplayVMOutput is true, display all VM output to stdout | false | bool |
| UseHeavyMonitors | use heavyweight instead of lightweight Java monitors | false | bool |
| RangeCheckElimination | Split loop iterations to eliminate range checks | true | bool |
| SplitIfBlocks | Clone compares and control flow through merge points to fold some branches | true | bool |
| AggressiveOpts | Enable aggressive optimizations - see arguments.cpp | false | bool |
| PrintInterpreter | Prints the generated interpreter code | false | bool |
| UseInterpreter | Use interpreter for non-compiled methods | true | bool |
| UseNiagaraInstrs | Use Niagara-efficient instruction subset | false | bool |
| UseLoopCounter | Increment invocation counter on backward branch | true | bool |
| UseFastEmptyMethods | Use fast method entry code for empty methods | true | bool |
| UseFastAccessorMethods | Use fast method entry code for accessor methods | true | bool |
| EnableJVMPIInstructionStartEvent | Enable JVMPI_EVENT_INSTRUCTION_START events - slows down interpretation | false | bool |
| JVMPICheckGCCompatibility | If JVMPI is used, make sure that we are using a JVMPI-compatible garbage collector | true | bool |
| ProfileMaturityPercentage | number of method invocations/branches (expressed as % of CompileThreshold) before using the method's profile | 20 | intx |
| UseCompiler | use compilation | true | bool |
| UseCounterDecay | adjust recompilation counters | true | bool |
| AlwaysCompileLoopMethods | when using recompilation, never interpret methods containing loops | false | bool |
| DontCompileHugeMethods | don't compile methods > HugeMethodLimit | true | bool |
| EstimateArgEscape | Analyze bytecodes to estimate escape state of arguments | true | bool |
| BCEATraceLevel | How much tracing to do of bytecode escape analysis estimates | 0 | intx |
| MaxBCEAEstimateLevel | Maximum number of nested calls that are analyzed by BC EA. | 5 | intx |
| MaxBCEAEstimateSize | Maximum bytecode size of a method to be analyzed by BC EA. | 150 | intx |
| SelfDestructTimer | Will cause VM to terminate after a given time (in minutes) (0 means off) | 0 | intx |
| MaxJavaStackTraceDepth | Max. no. of lines in the stack trace for Java exceptions (0 means all). With Java > 1.6, value 0 really means 0. value -1 or any negative number must be specified to print all the stack (tested with 1.6.0_22, 1.7.0 on Windows). With Java <= 1.5, value 0 means everything, JVM chokes on negative number (tested with 1.5.0_22 on Windows). | 1024 | intx |
| NmethodSweepFraction | Number of invocations of sweeper to cover all nmethods | 4 | intx |
| MaxInlineSize | maximum bytecode size of a method to be inlined | 35 | intx |
| ProfileIntervalsTicks | # of ticks between printing of interval profile (+ProfileIntervals) | 100 | intx |
| EventLogLength | maximum nof events in event log | 2000 | intx |
| PerMethodRecompilationCutoff | After recompiling N times, stay in the interpreter (-1=>'Inf') | 400 | intx |
| PerBytecodeRecompilationCutoff | Per-BCI limit on repeated recompilation (-1=>'Inf') | 100 | intx |
| PerMethodTrapLimit | Limit on traps (of one kind) in a method (includes inlines) | 100 | intx |
| PerBytecodeTrapLimit | Limit on traps (of one kind) at a particular BCI | 4 | intx |
| AliasLevel | 0 for no aliasing, 1 for oop/field/static/array split, 2 for best | 2 | intx |
| ReadSpinIterations | Number of read attempts before a yield (spin inner loop) | 100 | intx |
| PreBlockSpin | Number of times to spin in an inflated lock before going to an OS lock | 10 | intx |
| MaxHeapSize | Default maximum size for object heap (in bytes) | ScaleForWordSize (64*M) | uintx |
| MaxNewSize | Maximum size of new generation (in bytes) | max_uintx | uintx |
| PretenureSizeThreshold | Max size in bytes of objects allocated in DefNew generation | 0 | uintx |
| MinTLABSize | Minimum allowed TLAB size (in bytes) | 2*K | uintx |
| TLABAllocationWeight | Allocation averaging weight | 35 | uintx |
| TLABWasteTargetPercent | Percentage of Eden that can be wasted | 1 | uintx |
| TLABRefillWasteFraction | Max TLAB waste at a refill (internal fragmentation) | 64 | uintx |
| TLABWasteIncrement | Increment allowed waste at slow allocation | 4 | uintx |
| MaxLiveObjectEvacuationRatio | Max percent of eden objects that will be live at scavenge | 100 | uintx |
| OldSize | Default size of tenured generation (in bytes) | ScaleForWordSize (4096*K) | uintx |
| MinHeapFreeRatio | Min percentage of heap free after GC to avoid expansion | 40 | uintx |
| MaxHeapFreeRatio | Max percentage of heap free after GC to avoid shrinking | 70 | uintx |
| SoftRefLRUPolicyMSPerMB | Number of milliseconds per MB of free space in the heap | 1000 | intx |
| MinHeapDeltaBytes | Min change in heap space due to GC (in bytes) | ScaleForWordSize (128*K) | uintx |
| MinPermHeapExpansion | Min expansion of permanent heap (in bytes) | ScaleForWordSize (256*K) | uintx |
| MaxPermHeapExpansion | Max expansion of permanent heap without full GC (in bytes) | ScaleForWordSize (4*M) | uintx |
| QueuedAllocationWarningCount | Number of times an allocation that queues behind a GC will retry before printing a warning | 0 | intx |
| MaxTenuringThreshold | Maximum value for tenuring threshold. See more info about that flag here. | 15 | intx |
| InitialTenuringThreshold | Initial value for tenuring threshold | 7 | intx |
| TargetSurvivorRatio | Desired percentage of survivor space used after scavenge | 50 | intx |
| MarkSweepDeadRatio | Percentage (0-100) of the old gen allowed as dead wood. "Serial mark sweep treats this as both the min and max value." CMS uses this value only if it falls back to mark sweep." Par compact uses a variable scale based on the density of the" generation and treats this as the max value when the heap is" either completely full or completely empty. Par compact also" has a smaller default value; see arguments.cpp. | 5 | intx |
| PermMarkSweepDeadRatio | Percentage (0-100) of the perm gen allowed as dead wood." See MarkSweepDeadRatio for collector-specific comments. | 20 | intx |
| MarkSweepAlwaysCompactCount | How often should we fully compact the heap (ignoring the dead space parameters) | 4 | intx |
| PrintCMSStatistics | Statistics for CMS | 0 | intx |
| PrintCMSInitiationStatistics | Statistics for initiating a CMS collection | false | bool |
| PrintFLSStatistics | Statistics for CMS' FreeListSpace | 0 | intx |
| PrintFLSCensus | Census for CMS' FreeListSpace | 0 | intx |
| DeferThrSuspendLoopCount | (Unstable) Number of times to iterate in safepoint loop before blocking VM threads | 4000 | intx |
| DeferPollingPageLoopCount | (Unsafe,Unstable) Number of iterations in safepoint loop before changing safepoint polling page to RO | -1 | intx |
| SafepointSpinBeforeYield | (Unstable) | 2000 | intx |
| UseDepthFirstScavengeOrder | true: the scavenge order will be depth-first, false: the scavenge order will be breadth-first | true | bool |
| GCDrainStackTargetSize | how many entries we'll try to leave on the stack during parallel GC | 64 | uintx |
| ThreadSafetyMargin | Thread safety margin is used on fixed-stack LinuxThreads (on Linux/x86 only) to prevent heap-stack collision. Set to 0 to disable this feature | 50*M | uintx |
| CodeCacheMinimumFreeSpace | When less than X space left, we stop compiling. | 500*K | uintx |
| CompileOnly | List of methods (pkg/class.name) to restrict compilation to | "" | ccstr |
| CompileCommandFile | Read compiler commands from this file [.hotspot_compiler] | "" | ccstr |
| CompileCommand | Prepend to .hotspot_compiler; e.g. log,java/lang/String. | "" | ccstr |
| CICompilerCountPerCPU | 1 compiler thread for log(N CPUs) | false | bool |
| UseThreadPriorities | Use native thread priorities | true | bool |
| ThreadPriorityPolicy | 0 : Normal. VM chooses priorities that are appropriate for normal applications. On Solaris NORM_PRIORITY and above are mapped to normal native priority. Java priorities below NORM_PRIORITY" map to lower native priority values. On Windows applications" are allowed to use higher native priorities. However, with ThreadPriorityPolicy=0, VM will not use the highest possible" native priority, THREAD_PRIORITY_TIME_CRITICAL, as it may interfere with system threads. On Linux thread priorities are ignored because the OS does not support static priority in SCHED_OTHER scheduling class which is the only choice for" non-root, non-realtime applications. 1 : Aggressive. Java thread priorities map over to the entire range of native thread priorities. Higher Java thread priorities map to higher native thread priorities. This policy should be used with care, as sometimes it can cause performance degradation in the application and/or the entire system. On Linux this policy requires root privilege. | 0 | intx |
| ThreadPriorityVerbose | print priority changes | false | bool |
| DefaultThreadPriority | what native priority threads run at if not specified elsewhere (-1 means no change) | -1 | intx |
| CompilerThreadPriority | what priority should compiler threads run at (-1 means no change) | -1 | intx |
| VMThreadPriority | what priority should VM threads run at (-1 means no change) | -1 | intx |
| CompilerThreadHintNoPreempt | (Solaris only) Give compiler threads an extra quanta | true | bool |
| VMThreadHintNoPreempt | (Solaris only) Give VM thread an extra quanta | false | bool |
| JavaPriority1_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority2_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority3_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority4_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority5_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority6_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority7_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority8_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority9_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| JavaPriority10_To_OSPriority | Map Java priorities to OS priorities | -1 | intx |
| StarvationMonitorInterval | Pause between each check in ms | 200 | intx |
| Tier1BytecodeLimit | Must have at least this many bytecodes before tier1" invocation counters are used | 10 | intx |
| StressTieredRuntime | Alternate client and server compiler on compile requests | false | bool |
| InterpreterProfilePercentage | number of method invocations/branches (expressed as % of CompileThreshold) before profiling in the interpreter | 33 | intx |
| MaxDirectMemorySize | Maximum total size of NIO direct-buffer allocations | -1 | intx |
| UseUnsupportedDeprecatedJVMPI | Flag to temporarily re-enable the, soon to be removed, experimental interface JVMPI. | false | bool |
| UsePerfData | Flag to disable jvmstat instrumentation for performance testing" and problem isolation purposes. | true | bool |
| PerfDataSaveToFile | Save PerfData memory to hsperfdata_ file on exit | false | bool |
| PerfDataSamplingInterval | Data sampling interval in milliseconds | 50 /*ms*/ | intx |
| PerfDisableSharedMem | Store performance data in standard memory | false | bool |
| PerfDataMemorySize | Size of performance data memory region. Will be rounded up to a multiple of the native os page size. | 32*K | intx |
| PerfMaxStringConstLength | Maximum PerfStringConstant string length before truncation | 1024 | intx |
| PerfAllowAtExitRegistration | Allow registration of atexit() methods | false | bool |
| PerfBypassFileSystemCheck | Bypass Win32 file system criteria checks (Windows Only) | false | bool |
| UnguardOnExecutionViolation | Unguard page and retry on no-execute fault (Win32 only)" 0=off, 1=conservative, 2=aggressive | 0 | intx |
| ManagementServer | Create JMX Management Server | false | bool |
| DisableAttachMechanism | Disable mechanism that allows tools to attach to this VM | false | bool |
| StartAttachListener | Always start Attach Listener at VM startup | false | bool |
| UseSharedSpaces | Use shared spaces in the permanent generation | true | bool |
| RequireSharedSpaces | Require shared spaces in the permanent generation | false | bool |
| ForceSharedSpaces | Require shared spaces in the permanent generation | false | bool |
| DumpSharedSpaces | Special mode: JVM reads a class list, loads classes, builds shared spaces, and dumps the shared spaces to a file to be used in future JVM runs. | false | bool |
| PrintSharedSpaces | Print usage of shared spaces | false | bool |
| SharedDummyBlockSize | Size of dummy block used to shift heap addresses (in bytes) | 512*M | uintx |
| SharedReadWriteSize | Size of read-write space in permanent generation (in bytes) | 12*M | uintx |
| SharedReadOnlySize | Size of read-only space in permanent generation (in bytes) | 8*M | uintx |
| SharedMiscDataSize | Size of the shared data area adjacent to the heap (in bytes) | 4*M | uintx |
| SharedMiscCodeSize | Size of the shared code area adjacent to the heap (in bytes) | 4*M | uintx |
| TaggedStackInterpreter | Insert tags in interpreter execution stack for oopmap generaion | false | bool |
| ExtendedDTraceProbes | Enable performance-impacting dtrace probes | false | bool |
| DTraceMethodProbes | Enable dtrace probes for method-entry and method-exit | false | bool |
| DTraceAllocProbes | Enable dtrace probes for object allocation | false | bool |
| DTraceMonitorProbes | Enable dtrace probes for monitor events | false | bool |
| RelaxAccessControlCheck | Relax the access control checks in the verifier | false | bool |
| UseVMInterruptibleIO | (Unstable, Solaris-specific) Thread interrupt before or with EINTR for I/O operations results in OS_INTRPT | true | bool |
| AggressiveHeap | The option inspects the server resources (size of memory and number of processors), and attempts to set various parameters to be optimal for long-running, memory allocation-intensive jobs. The JVM team view AggressiveHeap as an anachronism and would like to see it go away. Instead, we'd prefer for you to determine which of the individual options that AggressiveHeap sets actually impact your app, and then set those on the command line directly. You can check the Open JDK source code to see what AggressiveHeap actually does (arguments.cpp) | false | bool |
| UseCompressedStrings | Use a byte[] for Strings which can be represented as pure ASCII. (Introduced in Java 6 Update 21 Performance Release) | false | bool |
| OptimizeStringConcat | Optimize String concatenation operations where possible. (Introduced in Java 6 Update 20) | false | bool |
| UseStringCache | Enables caching of commonly allocated strings. | false | bool |
| G1HeapRegionSize | With G1 the Java heap is subdivided into uniformly sized regions. This sets the size of the individual sub-divisions. The default value of this parameter is determined ergonomically based upon heap size. The minimum value is 1Mb and the maximum value is 32Mb. Introduced in Java 6 Update 26. | 8m |  |
| G1ReservePercent | Sets the amount of heap that is reserved as a false ceiling to reduce the possibility of promotion failure. Introduced in Java 6 Update 26. | 10 |  |
| G1ConfidencePercent | Confidence coefficient for G1 pause prediction. Introduced in Java 6 Update 26. | 50 |  |
| PrintPromotionFailure | Prints additional information on GC promotion failures. |  | bool |
| MANAGEABLE | | | |
| HeapDumpOnOutOfMemoryError | Dump heap to file when java.lang.OutOfMemoryError is thrown | false | bool |
| HeapDumpPath | When HeapDumpOnOutOfMemoryError is on, the path (filename or" directory) of the dump file (defaults to java_pid.hprof" in the working directory) | "" | ccstr |
| PrintGC | Print message at garbage collect | false | bool |
| PrintGCDetails | Print more details at garbage collect | false | bool |
| PrintGCTimeStamps | Print timestamps at garbage collect | false | bool |
| PrintGCDateStamps | Print datestamps (ISO_8601, e.g. 2013-10-18T12:32:01.657+0100) at garbage collect. Since Java 1.6.u4. | false | bool |
| PrintClassHistogram | Print a histogram of class instances | false | bool |
| PrintConcurrentLocks | Print java.util.concurrent locks in thread dump | false | bool |
| EXPERIMENTAL | | | |
| UnlockExperimentalVMOptions | Unlocks experimental options. | false | bool |
| UseG1GC | Switch on G1 for Java6. G1 is default for Java7, so there is no such option there. | false | bool |
| PRODUCT_RW | | | |
| TraceClassLoading | Trace all classes loaded | false | bool |
| TraceClassUnloading | Trace unloading of classes | false | bool |
| TraceLoaderConstraints | Trace loader constraints | false | bool |
| PrintHeapAtGC | Print heap layout before and after each GC | false | bool |
| DEVELOP | | | |
| TraceItables | Trace initialization and use of itables | false | bool |
| TracePcPatching | Trace usage of frame::patch_pc | false | bool |
| TraceJumps | Trace assembly jumps in thread ring buffer | false | bool |
| TraceRelocator | Trace the bytecode relocator | false | bool |
| TraceLongCompiles | Print out every time compilation is longer than a given threashold | false | bool |
| SafepointALot | Generates a lot of safepoints. Works with GuaranteedSafepointInterval | false | bool |
| BailoutToInterpreterForThrows | Compiled methods which throws/catches exceptions will be deopt and intp. | false | bool |
| NoYieldsInMicrolock | Disable yields in microlock | false | bool |
| TraceOopMapGeneration | Shows oopmap generation | false | bool |
| MethodFlushing | Reclamation of zombie and not-entrant methods | true | bool |
| VerifyStack | Verify stack of each thread when it is entering a runtime call | false | bool |
| TraceDerivedPointers | Trace traversal of derived pointers on stack | false | bool |
| InlineArrayCopy | inline arraycopy native that is known to be part of base library DLL | true | bool |
| InlineObjectHash | inline Object::hashCode() native that is known to be part of base library DLL | true | bool |
| InlineNatives | inline natives that are known to be part of base library DLL | true | bool |
| InlineMathNatives | inline SinD, CosD, etc. | true | bool |
| InlineClassNatives | inline Class.isInstance, etc | true | bool |
| InlineAtomicLong | inline sun.misc.AtomicLong | true | bool |
| InlineThreadNatives | inline Thread.currentThread, etc | true | bool |
| InlineReflectionGetCallerClass | inline sun.reflect.Reflection.getCallerClass(), known to be part of base library DLL | true | bool |
| InlineUnsafeOps | inline memory ops (native methods) from sun.misc.Unsafe | true | bool |
| ConvertCmpD2CmpF | Convert cmpD to cmpF when one input is constant in float range | true | bool |
| ConvertFloat2IntClipping | Convert float2int clipping idiom to integer clipping | true | bool |
| SpecialStringCompareTo | special version of string compareTo | true | bool |
| SpecialStringIndexOf | special version of string indexOf | true | bool |
| TraceCallFixup | traces all call fixups | false | bool |
| DeoptimizeALot | deoptimize at every exit from the runtime system | false | bool |
| DeoptimizeOnlyAt | a comma separated list of bcis to deoptimize at | "" | ccstr |
| Debugging | set when executing debug methods in debug.ccp (to prevent triggering assertions) | false | bool |
| TraceHandleAllocation | Prints out warnings when suspicious many handles are allocated | false | bool |
| ShowSafepointMsgs | Show msg. about safepoint synch. | false | bool |
| SafepointTimeout | Time out and warn or fail after SafepointTimeoutDelay milliseconds if failed to reach safepoint | false | bool |
| DieOnSafepointTimeout | Die upon failure to reach safepoint (see SafepointTimeout) | false | bool |
| ForceFloatExceptions | Force exceptions on FP stack under/overflow | trueInDebug | bool |
| SoftMatchFailure | If the DFA fails to match a node, print a message and bail out | trueInProduct | bool |
| VerifyStackAtCalls | Verify that the stack pointer is unchanged after calls | false | bool |
| TraceJavaAssertions | Trace java language assertions | false | bool |
| ZapDeadCompiledLocals | Zap dead locals in compiler frames | false | bool |
| UseMallocOnly | use only malloc/free for allocation (no resource area/arena) | false | bool |
| PrintMalloc | print all malloc/free calls | false | bool |
| ZapResourceArea | Zap freed resource/arena space with 0xABABABAB | trueInDebug | bool |
| ZapJNIHandleArea | Zap freed JNI handle space with 0xFEFEFEFE | trueInDebug | bool |
| ZapUnusedHeapArea | Zap unused heap space with 0xBAADBABE | trueInDebug | bool |
| PrintVMMessages | Print vm messages on console | true | bool |
| Verbose | Prints additional debugging information from other modes | false | bool |
| PrintMiscellaneous | Prints uncategorized debugging information (requires +Verbose) | false | bool |
| WizardMode | Prints much more debugging information | false | bool |
| SegmentedHeapDumpThreshold | Generate a segmented heap dump (JAVA PROFILE 1.0.2 format) when the heap usage is larger than this | 2*G | uintx |
| HeapDumpSegmentSize | Approximate segment size when generating a segmented heap dump | 1*G | uintx |
| BreakAtWarning | Execute breakpoint upon encountering VM warning | false | bool |
| TraceVMOperation | Trace vm operations | false | bool |
| UseFakeTimers | Tells whether the VM should use system time or a fake timer | false | bool |
| PrintAssembly | Print assembly code. Requires disassembler plugin, see details here. | false | bool |
| PrintNMethods | Print assembly code for nmethods when generated | false | bool |
| PrintNativeNMethods | Print assembly code for native nmethods when generated | false | bool |
| PrintDebugInfo | Print debug information for all nmethods when generated | false | bool |
| PrintRelocations | Print relocation information for all nmethods when generated | false | bool |
| PrintDependencies | Print dependency information for all nmethods when generated | false | bool |
| PrintExceptionHandlers | Print exception handler tables for all nmethods when generated | false | bool |
| InterceptOSException | Starts debugger when an implicit OS (e.g., NULL) exception happens | false | bool |
| PrintCodeCache2 | Print detailed info on the compiled_code cache when exiting | false | bool |
| PrintStubCode | Print generated stub code | false | bool |
| PrintJVMWarnings | Prints warnings for unimplemented JVM functions | false | bool |
| InitializeJavaLangSystem | Initialize java.lang.System - turn off for individual method debugging | true | bool |
| InitializeJavaLangString | Initialize java.lang.String - turn off for individual method debugging | true | bool |
| InitializeJavaLangExceptionsErrors | Initialize various error and exception classes - turn off for individual method debugging | true | bool |
| RegisterReferences | Tells whether the VM should register soft/weak/final/phantom references | true | bool |
| IgnoreRewrites | Supress rewrites of bytecodes in the oopmap generator. This is unsafe! | false | bool |
| PrintCodeCacheExtension | Print extension of code cache | false | bool |
| UsePrivilegedStack | Enable the security JVM functions | true | bool |
| IEEEPrecision | Enables IEEE precision (for INTEL only) | true | bool |
| ProtectionDomainVerification | Verifies protection domain before resolution in system dictionary | true | bool |
| DisableStartThread | Disable starting of additional Java threads (for debugging only) | false | bool |
| MemProfiling | Write memory usage profiling to log file | false | bool |
| UseDetachedThreads | Use detached threads that are recycled upon termination (for SOLARIS only) | true | bool |
| UsePthreads | Use pthread-based instead of libthread-based synchronization (SPARC only) | false | bool |
| UpdateHotSpotCompilerFileOnError | Should the system attempt to update the compiler file when an error occurs? | true | bool |
| LoadLineNumberTables | Tells whether the class file parser loads line number tables | true | bool |
| LoadLocalVariableTables | Tells whether the class file parser loads local variable tables | true | bool |
| LoadLocalVariableTypeTables | Tells whether the class file parser loads local variable type tables | true | bool |
| PreallocatedOutOfMemoryErrorCount | Number of OutOfMemoryErrors preallocated with backtrace | 4 | uintx |
| PrintBiasedLockingStatistics | Print statistics of biased locking in JVM | false | bool |
| TraceJVMPI | Trace JVMPI | false | bool |
| TraceJNICalls | Trace JNI calls | false | bool |
| TraceJNIHandleAllocation | Trace allocation/deallocation of JNI handle blocks | false | bool |
| TraceThreadEvents | Trace all thread events | false | bool |
| TraceBytecodes | Trace bytecode execution | false | bool |
| TraceClassInitialization | Trace class initialization | false | bool |
| TraceExceptions | Trace exceptions | false | bool |
| TraceICs | Trace inline cache changes | false | bool |
| TraceInlineCacheClearing | Trace clearing of inline caches in nmethods | false | bool |
| TraceDependencies | Trace dependencies | false | bool |
| VerifyDependencies | Exercise and verify the compilation dependency mechanism | trueInDebug | bool |
| TraceNewOopMapGeneration | Trace OopMapGeneration | false | bool |
| TraceNewOopMapGenerationDetailed | Trace OopMapGeneration: print detailed cell states | false | bool |
| TimeOopMap | Time calls to GenerateOopMap::compute_map() in sum | false | bool |
| TimeOopMap2 | Time calls to GenerateOopMap::compute_map() individually | false | bool |
| TraceMonitorMismatch | Trace monitor matching failures during OopMapGeneration | false | bool |
| TraceOopMapRewrites | Trace rewritting of method oops during oop map generation | false | bool |
| TraceSafepoint | Trace safepoint operations | false | bool |
| TraceICBuffer | Trace usage of IC buffer | false | bool |
| TraceCompiledIC | Trace changes of compiled IC | false | bool |
| TraceStartupTime | Trace setup time | false | bool |
| TraceHPI | Trace Host Porting Interface (HPI) | false | bool |
| TraceProtectionDomainVerification | Trace protection domain verifcation | false | bool |
| TraceClearedExceptions | Prints when an exception is forcibly cleared | false | bool |
| UseParallelOldGCChunkPointerCalc | In the Parallel Old garbage collector use chucks to calculate" new object locations | true | bool |
| VerifyParallelOldWithMarkSweep | Use the MarkSweep code to verify phases of Parallel Old | false | bool |
| VerifyParallelOldWithMarkSweepInterval | Interval at which the MarkSweep code is used to verify phases of Parallel Old | 1 | uintx |
| ParallelOldMTUnsafeMarkBitMap | Use the Parallel Old MT unsafe in marking the bitmap | false | bool |
| ParallelOldMTUnsafeUpdateLiveData | Use the Parallel Old MT unsafe in update of live size | false | bool |
| TraceChunkTasksQueuing | Trace the queuing of the chunk tasks | false | bool |
| ScavengeWithObjectsInToSpace | Allow scavenges to occur when to_space contains objects. | false | bool |
| UseCMSAdaptiveFreeLists | Use Adaptive Free Lists in the CMS generation | true | bool |
| UseAsyncConcMarkSweepGC | Use Asynchronous Concurrent Mark-Sweep GC in the old generation | true | bool |
| RotateCMSCollectionTypes | Rotate the CMS collections among concurrent and STW | false | bool |
| CMSTraceIncrementalMode | Trace CMS incremental mode | false | bool |
| CMSTraceIncrementalPacing | Trace CMS incremental mode pacing computation | false | bool |
| CMSTraceThreadState | Trace the CMS thread state (enable the trace_state() method) | false | bool |
| CMSDictionaryChoice | Use BinaryTreeDictionary as default in the CMS generation | 0 | intx |
| CMSOverflowEarlyRestoration | Whether preserved marks should be restored early | false | bool |
| CMSTraceSweeper | Trace some actions of the CMS sweeper | false | bool |
| FLSVerifyDictionary | Do lots of (expensive) FLS dictionary verification | false | bool |
| VerifyBlockOffsetArray | Do (expensive!) block offset array verification | false | bool |
| TraceCMSState | Trace the state of the CMS collection | false | bool |
| CMSTestInFreeList | Check if the coalesced range is already in the free lists as claimed. | false | bool |
| CMSIgnoreResurrection | Ignore object resurrection during the verification. | true | bool |
| FullGCALot | Force full gc at every Nth exit from the runtime system (N=FullGCALotInterval) | false | bool |
| PromotionFailureALotCount | Number of promotion failures occurring at ParGCAllocBuffer" refill attempts (ParNew) or promotion attempts (other young collectors) | 1000 | uintx |
| PromotionFailureALotInterval | Total collections between promotion failures alot | 5 | uintx |
| WorkStealingSleepMillis | Sleep time when sleep is used for yields | 1 | intx |
| WorkStealingYieldsBeforeSleep | Number of yields before a sleep is done during workstealing | 1000 | uintx |
| TraceAdaptiveGCBoundary | Trace young-old boundary moves | false | bool |
| PSAdaptiveSizePolicyResizeVirtualSpaceAlot | Resize the virtual spaces of the young or old generations | -1 | intx |
| PSAdjustTenuredGenForMinorPause | Adjust tenured generation to achive a minor pause goal | false | bool |
| PSAdjustYoungGenForMajorPause | Adjust young generation to achive a major pause goal | false | bool |
| AdaptiveSizePolicyReadyThreshold | Number of collections before the adaptive sizing is started | 5 | uintx |
| AdaptiveSizePolicyGCTimeLimitThreshold | Number of consecutive collections before gc time limit fires | 5 | uintx |
| UsePrefetchQueue | Use the prefetch queue during PS promotion | true | bool |
| ConcGCYieldTimeout | If non-zero, assert that GC threads yield within this # of ms. | 0 | intx |
| TraceReferenceGC | Trace handling of soft/weak/final/phantom references | false | bool |
| TraceFinalizerRegistration | Trace registration of final references | false | bool |
| TraceWorkGang | Trace activities of work gangs | false | bool |
| TraceBlockOffsetTable | Print BlockOffsetTable maps | false | bool |
| TraceCardTableModRefBS | Print CardTableModRefBS maps | false | bool |
| TraceGCTaskManager | Trace actions of the GC task manager | false | bool |
| TraceGCTaskQueue | Trace actions of the GC task queues | false | bool |
| TraceGCTaskThread | Trace actions of the GC task threads | false | bool |
| TraceParallelOldGCMarkingPhase | Trace parallel old gc marking phase | false | bool |
| TraceParallelOldGCSummaryPhase | Trace parallel old gc summary phase | false | bool |
| TraceParallelOldGCCompactionPhase | Trace parallel old gc compaction phase | false | bool |
| TraceParallelOldGCDensePrefix | Trace parallel old gc dense prefix computation | false | bool |
| IgnoreLibthreadGPFault | Suppress workaround for libthread GP fault | false | bool |
| CIPrintCompilerName | when CIPrint is active, print the name of the active compiler | false | bool |
| CIPrintCompileQueue | display the contents of the compile queue whenever a compilation is enqueued | false | bool |
| CIPrintRequests | display every request for compilation | false | bool |
| CITimeEach | display timing information after each successful compilation | false | bool |
| CICountOSR | use a separate counter when assigning ids to osr compilations | true | bool |
| CICompileNatives | compile native methods if supported by the compiler | true | bool |
| CIPrintMethodCodes | print method bytecodes of the compiled code | false | bool |
| CIPrintTypeFlow | print the results of ciTypeFlow analysis | false | bool |
| CITraceTypeFlow | detailed per-bytecode tracing of ciTypeFlow analysis | false | bool |
| CICloneLoopTestLimit | size limit for blocks heuristically cloned in ciTypeFlow | 100 | intx |
| UseStackBanging | use stack banging for stack overflow checks (required for proper StackOverflow handling; disable only to measure cost of stackbanging) | true | bool |
| Use24BitFPMode | Set 24-bit FPU mode on a per-compile basis | true | bool |
| Use24BitFP | use FP instructions that produce 24-bit precise results | true | bool |
| UseStrictFP | use strict fp if modifier strictfp is set | true | bool |
| GenerateSynchronizationCode | generate locking/unlocking code for synchronized methods and monitors | true | bool |
| GenerateCompilerNullChecks | Generate explicit null checks for loads/stores/calls | true | bool |
| GenerateRangeChecks | Generate range checks for array accesses | true | bool |
| PrintSafepointStatistics | print statistics about safepoint synchronization | false | bool |
| InlineAccessors | inline accessor methods (get/set) | true | bool |
| UseCHA | enable CHA | true | bool |
| PrintInlining | prints inlining optimizations | false | bool |
| EagerInitialization | Eagerly initialize classes if possible | false | bool |
| TraceMethodReplacement | Print when methods are replaced do to recompilation | false | bool |
| PrintMethodFlushing | print the nmethods being flushed | false | bool |
| UseRelocIndex | use an index to speed random access to relocations | false | bool |
| StressCodeBuffers | Exercise code buffer expansion and other rare state changes | false | bool |
| DebugVtables | add debugging code to vtable dispatch | false | bool |
| PrintVtables | print vtables when printing klass | false | bool |
| TraceCreateZombies | trace creation of zombie nmethods | false | bool |
| MonomorphicArrayCheck | Uncommon-trap array store checks that require full type check | true | bool |
| DelayCompilationDuringStartup | Delay invoking the compiler until main application class is loaded | true | bool |
| CompileTheWorld | Compile all methods in all classes in bootstrap class path (stress test) | false | bool |
| CompileTheWorldPreloadClasses | Preload all classes used by a class before start loading | true | bool |
| TraceIterativeGVN | Print progress during Iterative Global Value Numbering | false | bool |
| FillDelaySlots | Fill delay slots (on SPARC only) | true | bool |
| VerifyIterativeGVN | Verify Def-Use modifications during sparse Iterative Global Value Numbering | false | bool |
| TimeLivenessAnalysis | Time computation of bytecode liveness analysis | false | bool |
| TraceLivenessGen | Trace the generation of liveness analysis information | false | bool |
| PrintDominators | Print out dominator trees for GVN | false | bool |
| UseLoopSafepoints | Generate Safepoint nodes in every loop | true | bool |
| DeutschShiffmanExceptions | Fast check to find exception handler for precisely typed exceptions | true | bool |
| FastAllocateSizeLimit | Inline allocations larger than this in doublewords must go slow | 100000 | intx |
| UseVTune | enable support for Intel's VTune profiler | false | bool |
| CountCompiledCalls | counts method invocations | false | bool |
| CountJNICalls | counts jni method invocations | false | bool |
| ClearInterpreterLocals | Always clear local variables of interpreter activations upon entry | false | bool |
| UseFastSignatureHandlers | Use fast signature handlers for native calls | true | bool |
| UseV8InstrsOnly | Use SPARC-V8 Compliant instruction subset | false | bool |
| UseCASForSwap | Do not use swap instructions, but only CAS (in a loop) on SPARC | false | bool |
| PoisonOSREntry | Detect abnormal calls to OSR code | true | bool |
| CountBytecodes | Count number of bytecodes executed | false | bool |
| PrintBytecodeHistogram | Print histogram of the executed bytecodes | false | bool |
| PrintBytecodePairHistogram | Print histogram of the executed bytecode pairs | false | bool |
| PrintSignatureHandlers | Print code generated for native method signature handlers | false | bool |
| VerifyOops | Do plausibility checks for oops | false | bool |
| CheckUnhandledOops | Check for unhandled oops in VM code | false | bool |
| VerifyJNIFields | Verify jfieldIDs for instance fields | trueInDebug | bool |
| VerifyFPU | Verify FPU state (check for NaN's, etc.) | false | bool |
| VerifyThread | Watch the thread register for corruption (SPARC only) | false | bool |
| VerifyActivationFrameSize | Verify that activation frame didn't become smaller than its minimal size | false | bool |
| TraceFrequencyInlining | Trace frequency based inlining | false | bool |
| PrintMethodData | Print the results of +ProfileInterpreter at end of run | false | bool |
| VerifyDataPointer | Verify the method data pointer during interpreter profiling | trueInDebug | bool |
| TraceCompilationPolicy | Trace compilation policy | false | bool |
| TimeCompilationPolicy | Time the compilation policy | false | bool |
| CounterHalfLifeTime | half-life time of invocation counters (in secs) | 30 | intx |
| CounterDecayMinIntervalLength | Min. ms. between invocation of CounterDecay | 500 | intx |
| TraceDeoptimization | Trace deoptimization | false | bool |
| DebugDeoptimization | Tracing various information while debugging deoptimization | false | bool |
| GuaranteedSafepointInterval | Guarantee a safepoint (at least) every so many milliseconds (0 means none) | 1000 | intx |
| SafepointTimeoutDelay | Delay in milliseconds for option SafepointTimeout | 10000 | intx |
| MallocCatchPtr | Hit breakpoint when mallocing/freeing this pointer | -1 | intx |
| TotalHandleAllocationLimit | Threshold for total handle allocation when +TraceHandleAllocation is used | 1024 | uintx |
| StackPrintLimit | number of stack frames to print in VM-level stack dump | 100 | intx |
| MaxInlineLevel | maximum number of nested calls that are inlined | 9 | intx |
| MaxRecursiveInlineLevel | maximum number of nested recursive calls that are inlined | 1 | intx |
| InlineSmallCode | Only inline already compiled methods if their code size is less than this | 1000 | intx |
| MaxTrivialSize | maximum bytecode size of a trivial method to be inlined | 6 | intx |
| MinInliningThreshold | min. invocation count a method needs to have to be inlined | 250 | intx |
| AlignEntryCode | aligns entry code to specified value (in bytes) | 4 | intx |
| MethodHistogramCutoff | cutoff value for method invoc. histogram (+CountCalls) | 100 | intx |
| ProfilerNumberOfInterpretedMethods | # of interpreted methods to show in profile | 25 | intx |
| ProfilerNumberOfCompiledMethods | # of compiled methods to show in profile | 25 | intx |
| ProfilerNumberOfStubMethods | # of stub methods to show in profile | 25 | intx |
| ProfilerNumberOfRuntimeStubNodes | # of runtime stub nodes to show in profile | 25 | intx |
| DontYieldALotInterval | Interval between which yields will be dropped (milliseconds) | 10 | intx |
| MinSleepInterval | Minimum sleep() interval (milliseconds) when ConvertSleepToYield is off (used for SOLARIS) | 1 | intx |
| ProfilerPCTickThreshold | Number of ticks in a PC buckets to be a hotspot | 15 | intx |
| StressNonEntrant | Mark nmethods non-entrant at registration | false | bool |
| TypeProfileWidth | number of receiver types to record in call profile | 2 | intx |
| BciProfileWidth | number of return bci's to record in ret profile | 2 | intx |
| FreqCountInvocations | Scaling factor for branch frequencies (deprecated) | 1 | intx |
| InlineFrequencyRatio | Ratio of call site execution to caller method invocation | 20 | intx |
| InlineThrowCount | Force inlining of interpreted methods that throw this often | 50 | intx |
| InlineThrowMaxSize | Force inlining of throwing methods smaller than this | 200 | intx |
| VerifyAliases | perform extra checks on the results of alias analysis | false | bool |
| ProfilerNodeSize | Size in K to allocate for the Profile Nodes of each thread | 1024 | intx |
| V8AtomicOperationUnderLockSpinCount | Number of times to spin wait on a v8 atomic operation lock | 50 | intx |
| ExitAfterGCNum | If non-zero, exit after this GC. | 0 | uintx |
| GCExpandToAllocateDelayMillis | Delay in ms between expansion and allocation | 0 | uintx |
| CodeCacheSegmentSize | Code cache segment size (in bytes) - smallest unit of allocation | 64 | uintx |
| BinarySwitchThreshold | Minimal number of lookupswitch entries for rewriting to binary switch | 5 | intx |
| StopInterpreterAt | Stops interpreter execution at specified bytecode number | 0 | intx |
| TraceBytecodesAt | Traces bytecodes starting with specified bytecode number | 0 | intx |
| CIStart | the id of the first compilation to permit | 0 | intx |
| CIStop | the id of the last compilation to permit | -1 | intx |
| CIStartOSR | the id of the first osr compilation to permit (CICountOSR must be on) | 0 | intx |
| CIStopOSR | the id of the last osr compilation to permit (CICountOSR must be on) | -1 | intx |
| CIBreakAtOSR | id of osr compilation to break at | -1 | intx |
| CIBreakAt | id of compilation to break at | -1 | intx |
| CIFireOOMAt | Fire OutOfMemoryErrors throughout CI for testing the compiler (non-negative value throws OOM after this many CI accesses in each compile) | -1 | intx |
| CIFireOOMAtDelay | Wait for this many CI accesses to occur in all compiles before beginning to throw OutOfMemoryErrors in each compile | -1 | intx |
| NewCodeParameter | Testing Only: Create a dedicated integer parameter before putback | 0 | intx |
| MinOopMapAllocation | Minimum number of OopMap entries in an OopMapSet | 8 | intx |
| LongCompileThreshold | Used with +TraceLongCompiles | 50 | intx |
| MaxRecompilationSearchLength | max. # frames to inspect searching for recompilee | 10 | intx |
| MaxInterpretedSearchLength | max. # interp. frames to skip when searching for recompilee | 3 | intx |
| DesiredMethodLimit | desired max. method size (in bytecodes) after inlining | 8000 | intx |
| HugeMethodLimit | don't compile methods larger than this if +DontCompileHugeMethods | 8000 | intx |
| UseNewReflection | Temporary flag for transition to reflection based on dynamic bytecode generation in 1.4; can no longer be turned off in 1.4 JDK, and is unneeded in 1.3 JDK, but marks most places VM changes were needed | true | bool |
| VerifyReflectionBytecodes | Force verification of 1.4 reflection bytecodes. Does not work in situations like that described in 4486457 or for constructors generated for serialization, so can not be enabled in product. | false | bool |
| FastSuperclassLimit | Depth of hardwired instanceof accelerator array | 8 | intx |
| PerfTraceDataCreation | Trace creation of Performance Data Entries | false | bool |
| PerfTraceMemOps | Trace PerfMemory create/attach/detach calls | false | bool |
| SharedOptimizeColdStartPolicy | Reordering policy for SharedOptimizeColdStart 0=favor classload-time locality, 1=balanced, 2=favor runtime locality | 2 | intx |
| PRODUCT_PD | | | |
| UseLargePages | Use large page memory |  | bool |
| UseSSE | 0=fpu stack,1=SSE for floats,2=SSE/SSE2 for all (x86/amd only) |  | intx |
| UseISM | Use Intimate Shared Memory. [Not accepted for non-Solaris platforms.] For details, see Intimate Shared Memory. | true | bool |
| UseMPSS | Use Multiple Page Size Support w/4mb pages for the heap. Do not use with ISM as this replaces the need for ISM. (Introduced in 1.4.0 update 1, Relevant to Solaris 9 and newer.) [1.4.1 and earlier: false] | false | bool |
| BackgroundCompilation | A thread requesting compilation is not blocked during compilation |  | bool |
| UseVectoredExceptions | Temp Flag - Use Vectored Exceptions rather than SEH (Windows Only) |  | bool |
| DontYieldALot | Throw away obvious excess yield calls (for SOLARIS only) |  | bool |
| ConvertSleepToYield | Converts sleep(0) to thread yield (may be off for SOLARIS to improve GUI) |  | bool |
| UseTLAB | Use thread-local object allocation |  | bool |
| ResizeTLAB | Dynamically resize tlab size for threads |  | bool |
| NeverActAsServerClassMachine | Never act like a server-class machine |  | bool |
| PrefetchCopyIntervalInBytes | How far ahead to prefetch destination area (<= 0 means off) |  | intx |
| PrefetchScanIntervalInBytes | How far ahead to prefetch scan area (<= 0 means off) |  | intx |
| PrefetchFieldsAhead | How many fields ahead to prefetch in oop scan (<= 0 means off) |  | intx |
| CompilationPolicyChoice | which compilation policy |  | intx |
| RewriteBytecodes | Allow rewriting of bytecodes (bytecodes are not immutable) |  | bool |
| RewriteFrequentPairs | Rewrite frequently used bytecode pairs into a single bytecode |  | bool |
| UseOnStackReplacement | Use on stack replacement, calls runtime if invoc. counter overflows in loop |  | bool |
| PreferInterpreterNativeStubs | Use always interpreter stubs for native methods invoked via interpreter |  | bool |
| AllocatePrefetchStyle | 0=no prefetch, 1=dead load, 2=prefetch instruction |  | intx |
| AllocatePrefetchDistance | Distance to prefetch ahead of allocation pointer |  | intx |
| FreqInlineSize | maximum bytecode size of a frequent method to be inlined |  | intx |
| PreInflateSpin | Number of times to spin wait before inflation |  | intx |
| NewSize | Default size of new generation (in bytes) |  | uintx |
| TLABSize | Default (or starting) size of TLAB (in bytes) |  | uintx |
| SurvivorRatio | Ratio of eden/survivor space size |  | intx |
| NewRatio | Ratio of new/old generation sizes |  | intx |
| NewSizeThreadIncrease | Additional size added to desired new generation size per non-daemon thread (in bytes) |  | uintx |
| PermSize | Default size of permanent generation (in bytes) |  | uintx |
| MaxPermSize | Maximum size of permanent generation (in bytes) |  | uintx |
| StackYellowPages | Number of yellow zone (recoverable overflows) pages |  | intx |
| StackRedPages | Number of red zone (unrecoverable overflows) pages |  | intx |
| StackShadowPages | Number of shadow zone (for overflow checking) pages this should exceed the depth of the VM and native call stack. In the HotSpot implementation, Java methods share stack frames with C/C++ native code, namely user native code and the virtual machine itself. Java methods generate code that checks that stack space is available a fixed distance towards the end of the stack so that the native code can be called without exceeding the stack space. This distance towards the end of the stack is called “Shadow Pages”. The page size usually is 4096b, which mean that 20 pages would occupy 90Kb. See some more info on that parameter in bug 7059899 and Crash due to Stack Overflow section of "Troubleshooting System Crashes" from Oracle. | Depends on machine. It's 3 on x86, 6 on amd64, etc | intx |
| ThreadStackSize | Thread Stack Size (in Kbytes) |  | intx |
| VMThreadStackSize | Non-Java Thread Stack Size (in Kbytes) |  | intx |
| CompilerThreadStackSize | Compiler Thread Stack Size (in Kbytes) |  | intx |
| InitialCodeCacheSize | Initial code cache size (in bytes) |  | uintx |
| ReservedCodeCacheSize | Reserved code cache size (in bytes) - maximum code cache size |  | uintx |
| CodeCacheExpansionSize | Code cache expansion size (in bytes) |  | uintx |
| CompileThreshold | number of method invocations/branches before (re-)compiling | 10000 | intx |
| Tier2CompileThreshold | threshold at which a tier 2 compilation is invoked |  | intx |
| Tier2BackEdgeThreshold | Back edge threshold at which a tier 2 compilation is invoked |  | intx |
| TieredCompilation | Enable two-tier compilation |  | bool |
| OnStackReplacePercentage | number of method invocations/branches (expressed as % of CompileThreshold) before (re-)compiling OSR code |  | intx |
| DEVELOP_PD | | | |
| ShareVtableStubs | Share vtable stubs (smaller code but worse branch prediction |  | bool |
| CICompileOSR | compile on stack replacement methods if supported by the compiler |  | bool |
| ImplicitNullChecks | generate code for implicit null checks |  | bool |
| UncommonNullCast | Uncommon-trap NULLs passed to check cast |  | bool |
| InlineIntrinsics | Inline intrinsics that can be statically resolved |  | bool |
| ProfileInterpreter | Profile at the bytecode level during interpretation |  | bool |
| ProfileTraps | Profile deoptimization traps at the bytecode level |  | bool |
| InlineFrequencyCount | Count of call site execution necessary to trigger frequent inlining |  | intx |
| JVMInvokeMethodSlack | Stack space (bytes) required for JVM_InvokeMethod to complete |  | uintx |
| CodeEntryAlignment | Code entry alignment for generated code (in bytes) |  | intx |
| CodeCacheMinBlockLength | Minimum number of segments in a code cache block. |  | uintx |
| NOTPRODUCT | | | |
| StressDerivedPointers | Force scavenge when a derived pointers is detected on stack after rtm call | false | bool |
| TraceCodeBlobStacks | Trace stack-walk of codeblobs | false | bool |
| PrintRewrites | Print methods that are being rewritten | false | bool |
| DeoptimizeRandom | deoptimize random frames on random exit from the runtime system | false | bool |
| ZombieALot | creates zombies (non-entrant) at exit from the runt. system | false | bool |
| WalkStackALot | trace stack (no print) at every exit from the runtime system | false | bool |
| StrictSafepointChecks | Enable strict checks that safepoints cannot happen for threads that used No_Safepoint_Verifier | trueInDebug | bool |
| VerifyLastFrame | Verify oops on last frame on entry to VM | false | bool |
| LogEvents | Enable Event log | trueInDebug | bool |
| CheckAssertionStatusDirectives | temporary - see javaClasses.cpp | false | bool |
| PrintMallocFree | Trace calls to C heap malloc/free allocation | false | bool |
| PrintOopAddress | Always print the location of the oop | false | bool |
| VerifyCodeCacheOften | Verify compiled-code cache often | false | bool |
| ZapDeadLocalsOld | Zap dead locals (old version, zaps all frames when entering the VM | false | bool |
| CheckOopishValues | Warn if value contains oop ( requires ZapDeadLocals) | false | bool |
| ZapVMHandleArea | Zap freed VM handle space with 0xBCBCBCBC | trueInDebug | bool |
| PrintCompilation2 | Print additional statistics per compilation | false | bool |
| PrintAdapterHandlers | Print code generated for i2c/c2i adapters | false | bool |
| PrintCodeCache | Print the compiled_code cache when exiting | false | bool |
| ProfilerCheckIntervals | Collect and print info on spacing of profiler ticks | false | bool |
| WarnOnStalledSpinLock | Prints warnings for stalled SpinLocks | 0 | uintx |
| PrintSystemDictionaryAtExit | Prints the system dictionary at exit | false | bool |
| ValidateMarkSweep | Do extra validation during MarkSweep collection | false | bool |
| RecordMarkSweepCompaction | Enable GC-to-GC recording and querying of compaction during MarkSweep | false | bool |
| TraceRuntimeCalls | Trace run-time calls | false | bool |
| TraceJVMCalls | Trace JVM calls | false | bool |
| TraceInvocationCounterOverflow | Trace method invocation counter overflow | false | bool |
| TraceZapDeadLocals | Trace zapping dead locals | false | bool |
| CMSMarkStackOverflowALot | Whether we should simulate frequent marking stack / work queue" overflow | false | bool |
| CMSMarkStackOverflowInterval | A per-thread `interval' counter that determines how frequently" we simulate overflow; a smaller number increases frequency | 1000 | intx |
| CMSVerifyReturnedBytes | Check that all the garbage collected was returned to the free lists. | false | bool |
| ScavengeALot | Force scavenge at every Nth exit from the runtime system (N=ScavengeALotInterval) | false | bool |
| GCALotAtAllSafepoints | Enforce ScavengeALot/GCALot at all potential safepoints | false | bool |
| PromotionFailureALot | Use promotion failure handling on every youngest generation collection | false | bool |
| CheckMemoryInitialization | Checks memory initialization | false | bool |
| TraceMarkSweep | Trace mark sweep | false | bool |
| PrintReferenceGC | Print times spent handling reference objects during GC (enabled only when PrintGCDetails) | false | bool |
| TraceScavenge | Trace scavenge | false | bool |
| TimeCompiler | time the compiler | false | bool |
| TimeCompiler2 | detailed time the compiler (requires +TimeCompiler) | false | bool |
| LogMultipleMutexLocking | log locking and unlocking of mutexes (only if multiple locks are held) | false | bool |
| PrintSymbolTableSizeHistogram | print histogram of the symbol table | false | bool |
| ExitVMOnVerifyError | standard exit from VM if bytecode verify error (only in debug mode) | false | bool |
| AbortVMOnException | Call fatal if this exception is thrown. Example: java -XX:AbortVMOnException=java.lang.NullPointerException Foo | "" | ccstr |
| PrintVtableStats | print vtables stats at end of run | false | bool |
| IgnoreLockingAssertions | disable locking assertions (for speed) | false | bool |
| VerifyLoopOptimizations | verify major loop optimizations | false | bool |
| CompileTheWorldIgnoreInitErrors | Compile all methods although class initializer failed | false | bool |
| TracePhaseCCP | Print progress during Conditional Constant Propagation | false | bool |
| TraceLivenessQuery | Trace queries of liveness analysis information | false | bool |
| CollectIndexSetStatistics | Collect information about IndexSets | false | bool |
| TraceCISCSpill | Trace allocators use of cisc spillable instructions | false | bool |
| TraceSpilling | Trace spilling | false | bool |
| CountVMLocks | counts VM internal lock attempts and contention | false | bool |
| CountRuntimeCalls | counts VM runtime calls | false | bool |
| CountJVMCalls | counts jvm method invocations | false | bool |
| CountRemovableExceptions | count exceptions that could be replaced by branches due to inlining | false | bool |
| ICMissHistogram | produce histogram of IC misses | false | bool |
| PrintClassStatistics | prints class statistics at end of run | false | bool |
| PrintMethodStatistics | prints method statistics at end of run | false | bool |
| TraceOnStackReplacement | Trace on stack replacement | false | bool |
| VerifyJNIEnvThread | Verify JNIEnv.thread == Thread::current() when entering VM from JNI | false | bool |
| TraceTypeProfile | Trace type profile | false | bool |
| MemProfilingInterval | Time between each invocation of the MemProfiler | 500 | intx |
| AssertRepeat | number of times to evaluate expression in assert (to estimate overhead); only works with -DUSE_REPEATED_ASSERTS | 1 | intx |
| SuppressErrorAt | List of assertions (file:line) to muzzle | "" | ccstr |
| HandleAllocationLimit | Threshold for HandleMark allocation when +TraceHandleAllocation is used | 1024 | uintx |
| MaxElementPrintSize | maximum number of elements to print | 256 | intx |
| MaxSubklassPrintSize | maximum number of subklasses to print when printing klass | 4 | intx |
| ScavengeALotInterval | Interval between which scavenge will occur with +ScavengeALot | 1 | intx |
| FullGCALotInterval | Interval between which full gc will occur with +FullGCALot | 1 | intx |
| FullGCALotStart | For which invocation to start FullGCAlot | 0 | intx |
| FullGCALotDummies | Dummy object allocated with +FullGCALot, forcing all objects to move | 32*K | intx |
| DeoptimizeALotInterval | Number of exits until DeoptimizeALot kicks in | 5 | intx |
| ZombieALotInterval | Number of exits until ZombieALot kicks in | 5 | intx |
| ExitOnFullCodeCache | Exit the VM if we fill the code cache. | false | bool |
| CompileTheWorldStartAt | First class to consider when using +CompileTheWorld | 1 | intx |
| CompileTheWorldStopAt | Last class to consider when using +CompileTheWorld | max_jint | intx |
| DIAGNOSTIC | | | |
| PrintFlagsFinal | Prints list of all available java paramenters. Information is displayed in 4 columns. First one is the type of parameter, second is parameter name, third is default value and the fourth is the type of the flag, i.e. product, diagnostic, C1 product (only for client JVM), C2 product (only for server JVM), etc. Available since 1.6. |  |  |
| UnlockDiagnosticVMOptions | Enable processing of flags relating to field diagnostics | trueInDebug | bool |
| LogCompilation | Log compilation activity in detail to hotspot.log or LogFile | false | bool |
| UnsyncloadClass | Unstable: VM calls loadClass unsynchronized. Custom classloader must call VM synchronized for findClass & defineClass | false | bool |
| FLSVerifyAllHeapReferences | Verify that all refs across the FLS boundary are to valid objects | false | bool |
| FLSVerifyLists | Do lots of (expensive) FreeListSpace verification | false | bool |
| FLSVerifyIndexTable | Do lots of (expensive) FLS index table verification | false | bool |
| VerifyBeforeExit | Verify system before exiting | trueInDebug | bool |
| VerifyBeforeGC | Verify memory system before GC | false | bool |
| VerifyAfterGC | Verify memory system after GC | false | bool |
| VerifyDuringGC | Verify memory system during GC (between phases) | false | bool |
| VerifyRememberedSets | Verify GC remembered sets | false | bool |
| VerifyObjectStartArray | Verify GC object start array if verify before/after | true | bool |
| BindCMSThreadToCPU | Bind CMS Thread to CPU if possible | false | bool |
| CPUForCMSThread | When BindCMSThreadToCPU is true, the CPU to bind CMS thread to | 0 | uintx |
| TraceJVMTIObjectTagging | Trace JVMTI object tagging calls | false | bool |
| VerifyBeforeIteration | Verify memory system before JVMTI iteration | false | bool |
| DebugNonSafepoints | Generate extra debugging info for non-safepoints in nmethods | trueInDebug | bool |
| SerializeVMOutput | Use a mutex to serialize output to tty and hotspot.log | true | bool |
| DisplayVMOutput | Display all VM output on the tty, independently of LogVMOutput | true | bool |
| LogVMOutput | Save VM output to hotspot.log, or to LogFile | trueInDebug | bool |
| LogFile | If LogVMOutput is on, save VM output to this file [hotspot.log] | "" | ccstr |
| MallocVerifyInterval | if non-zero, verify C heap after every N calls to malloc/realloc/free | 0 | intx |
| MallocVerifyStart | if non-zero, start verifying C heap after Nth call to malloc/realloc/free | 0 | intx |
| VerifyGCStartAt | GC invoke count where +VerifyBefore/AfterGC kicks in | 0 | uintx |
| VerifyGCLevel | Generation level at which to start +VerifyBefore/AfterGC | 0 | intx |
| UseNewCode | Testing Only: Use the new version while testing | false | bool |
| UseNewCode2 | Testing Only: Use the new version while testing | false | bool |
| UseNewCode3 | Testing Only: Use the new version while testing | false | bool |
| SharedOptimizeColdStart | At dump time, order shared objects to achieve better cold startup time. | true | bool |
| SharedSkipVerify | Skip assert() and verify() which page-in unwanted shared objects. | false | bool |
| PauseAtStartup | Causes the VM to pause at startup time and wait for the pause file to be removed (default: ./vm.paused.) | false | bool |
| PauseAtStartupFile | The file to create and for whose removal to await when pausing at startup. (default: ./vm.paused.) | "" | ccstr |

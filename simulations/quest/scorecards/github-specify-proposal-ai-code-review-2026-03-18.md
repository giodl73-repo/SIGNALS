● Read CLAUDE.md
  └ 88 lines read

● Read PRINCIPLES.md
  └ 262 lines read

● List directory signals
  └ 135 files found

● Search (glob)
  │ "signals/**/ai-code-review-*"
  └ 1 file found

Found one prior signal. Let me read it and the skill definition.

● List directory signals
  └ 135 files found

● Read ai-code-review-inertia-2026-03-18.md
  │ signals\discover\inertia\ai-code-review-inertia-2026-03-18.md
  └ 82 lines read

● Read specify-proposal.md
  │ signals\specify-proposal.md
  └ 152 lines read

Good — I have the inertia signal and the skill template. Let me check directory structure and read the review-code skill for context on the feature.

● Read review-code.md
  │ signals\review-code.md
  └ 7 lines read

● List directory signals\discover
  └ 1 file found



#
# Fatal process out of memory: Zone
#
----- Native stack trace -----

 1: 00007FF70433D52D node::MultiIsolatePlatform::DisposeIsolate+5341
 2: 00007FF70578C206 v8::base::FatalOOM+54
 3: 00007FF70502D9C5 v8::Function::NewInstance+245
 4: 00007FF7049A8A46 v8::SnapshotCreator::GetIsolate+56566
 5: 00007FF705BFF69A v8::base::DiyFp::Multiply+2470186
 6: 00007FF705BFED8B v8::base::DiyFp::Multiply+2467867
 7: 00007FF705BFE24D v8::base::DiyFp::Multiply+2464989
 8: 00007FF705BFDD24 v8::base::DiyFp::Multiply+2463668
 9: 00007FF705BFD2B1 v8::base::DiyFp::Multiply+2460993
10: 00007FF705BFD00F v8::base::DiyFp::Multiply+2460319
11: 00007FF705A09A46 v8::base::DiyFp::Multiply+414934
12: 00007FF705A08760 v8::base::DiyFp::Multiply+410096
13: 00007FF7057EC4EB v8::internal::compiler::CompilationDependencies::FieldTypeDependencyOffTheRecord+192907
14: 00007FF7046A2346 DSA_get0_engine+659126
15: 00007FF70469DA83 DSA_get0_engine+640499
16: 00007FF70469D369 DSA_get0_engine+638681
17: 00007FF7057FFDDF v8::base::SysInfo::AddressSpaceEnd+3167
18: 00007FF7043393EE node::GetNodeReport+89326
19: 00007FF705082DE6 uv_thread_detach+150
20: 00007FF7062C4173 v8::base::UnsignedDivisionByConstant<unsigned __int64>+2903907
21: 00007FFA6549E8D7 BaseThreadInitThunk+23
22: 00007FFA6666C53C RtlUserThreadStart+44

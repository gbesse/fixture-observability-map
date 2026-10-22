from itertools import combinations
from .common import identifier,integer,unique_ids

def run(data):
    faults=data['faults'];tests=data['tests']
    if not 1<=len(faults)<=64 or len(tests)>16:raise ValueError('size')
    if len(set(faults))!=len(faults):raise ValueError('duplicate_fault')
    for f in faults:identifier(f)
    unique_ids(tests);pairs=list(combinations(faults,2));coverage=[];universe=0
    for t in tests:
        integer(t['cost'],0,10**9)
        if set(t['outcomes'])!=set(faults):raise ValueError('outcome_coverage')
        for v in t['outcomes'].values():identifier(v)
        bits=sum(1<<i for i,(a,b) in enumerate(pairs) if t['outcomes'][a]!=t['outcomes'][b]);coverage.append(bits);universe|=bits
    indistinguishable=[list(pair) for i,pair in enumerate(pairs) if not (universe>>i&1)]
    costs=[0]*(1<<len(tests));covers=[0]*(1<<len(tests));best=None
    for mask in range(1<<len(tests)):
        if mask:
            bit=mask&-mask;i=bit.bit_length()-1;old=mask^bit;costs[mask]=costs[old]+tests[i]['cost'];covers[mask]=covers[old]|coverage[i]
        if covers[mask]==universe:
            ids=tuple(sorted(t['id'] for i,t in enumerate(tests) if mask>>i&1));candidate=(costs[mask],len(ids),ids,mask)
            if best is None or candidate<best:best=candidate
    chosen=[t for i,t in enumerate(tests) if best[3]>>i&1];signatures={f:tuple(t['outcomes'][f] for t in chosen) for f in faults};groups={}
    for f,signature in signatures.items():groups.setdefault(signature,[]).append(f)
    return {'all_faults_identifiable':not indistinguishable,'indistinguishable_pairs':indistinguishable,'minimum_cost':best[0],'selected_tests':list(best[2]),'equivalence_classes':sorted(groups.values()),'distinguishable_pair_count':universe.bit_count()}

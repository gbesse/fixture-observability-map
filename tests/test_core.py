import unittest,itertools
from fixture_observability_map import run
class DomainTests(unittest.TestCase):
 def test_hidden_ambiguity_not_claimed_identified(self):
  r=run({'faults':['a','b','c'],'tests':[{'id':'x','cost':2,'outcomes':{'a':'0','b':'0','c':'1'}}]});self.assertFalse(r['all_faults_identifiable']);self.assertEqual(r['indistinguishable_pairs'],[['a','b']])
 def test_cheaper_equivalent_test_selected(self):
  r=run({'faults':['a','b'],'tests':[{'id':'expensive','cost':10,'outcomes':{'a':'0','b':'1'}},{'id':'cheap','cost':1,'outcomes':{'a':'0','b':'1'}}]});self.assertEqual(r['selected_tests'],['cheap'])
 def test_combination_needed(self):
  fs=['00','01','10','11'];ts=[{'id':str(i),'cost':i+1,'outcomes':{f:f[i] for f in fs}} for i in (0,1)];r=run({'faults':fs,'tests':ts});self.assertTrue(r['all_faults_identifiable']);self.assertEqual(r['minimum_cost'],3)
 def test_no_tests(self):self.assertEqual(run({'faults':['a','b'],'tests':[]})['equivalence_classes'],[['a','b']])
 def test_missing_outcome_invalid(self):
  with self.assertRaises(ValueError):run({'faults':['a','b'],'tests':[{'id':'x','cost':1,'outcomes':{'a':'0'}}]})
 def test_single_hypothesis_no_test_needed(self):self.assertEqual(run({'faults':['a'],'tests':[]})['selected_tests'],[])

from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_18_00_e_REF_FINREP_3_0_UnionItem:
	base = None #F_18_00_e_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.base.NMNL_AMNT()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.PRFRMNG_STTS()
	@lineage(dependencies={"base.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.IMPRMNT_STTS()
	@lineage(dependencies={"base.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.DFLT_STTS()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()

class F_18_00_e_REF_FINREP_3_0_Base:
	def NMNL_AMNT() -> int:
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def PRFRMNG_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def IMPRMNT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def DFLT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass

class F_18_00_e_REF_FINREP_3_0_UnionTable :
	F_18_00_e_REF_FINREP_3_0_UnionItems = [] # F_18_00_e_REF_FINREP_3_0_UnionItem []
	F_18_00_e_REF_FINREP_3_0_Financial_guarantees_given_Table = None # Financial_guarantees_given
	F_18_00_e_REF_FINREP_3_0_Off_balance_sheet_exposures_subject_to_credit_risk_Table = None # Off_balance_sheet_exposures_subject_to_credit_risk
	def calc_F_18_00_e_REF_FINREP_3_0_UnionItems(self) -> list[F_18_00_e_REF_FINREP_3_0_UnionItem] :
		items = [] # F_18_00_e_REF_FINREP_3_0_UnionItem []
		for item in self.F_18_00_e_REF_FINREP_3_0_Financial_guarantees_given_Table.Financial_guarantees_givens:
			newItem = F_18_00_e_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_18_00_e_REF_FINREP_3_0_Off_balance_sheet_exposures_subject_to_credit_risk_Table.Off_balance_sheet_exposures_subject_to_credit_risks:
			newItem = F_18_00_e_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_18_00_e_REF_FINREP_3_0_UnionItems = []
		self.F_18_00_e_REF_FINREP_3_0_UnionItems.extend(self.calc_F_18_00_e_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Financial_guarantees_given(F_18_00_e_REF_FINREP_3_0_Base):
	CRDT_FCLTY = None # CRDT_FCLTY
	@lineage(dependencies={"CRDT_FCLTY.NMNL_AMNT"})
	def NMNL_AMNT(self):
		return self.CRDT_FCLTY.NMNL_AMNT
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self):
		return self.CRDT_FCLTY.PRFRMNG_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def IMPRMNT_STTS(self):
		return self.CRDT_FCLTY.PRFRMNG_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS
	@lineage(dependencies={"CRDT_FCLTY.DFLT_STTS_DRVD"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.DFLT_STTS_DRVD
	@lineage(dependencies={"CRDT_FCLTY.IMPRMNT_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.IMPRMNT_STTS
	@lineage(dependencies={"CRDT_FCLTY.PRFRMNG_STTS"})
	def DFLT_STTS(self):
		return self.CRDT_FCLTY.PRFRMNG_STTS

class Off_balance_sheet_exposures_subject_to_credit_risk(F_18_00_e_REF_FINREP_3_0_Base):
	pass

class F_18_00_e_REF_FINREP_3_0_Financial_guarantees_given_Table:
	CRDT_FCLTY_Table = None # CRDT_FCLTY
	Financial_guarantees_givens = []# Financial_guarantees_given[]
	def calc_Financial_guarantees_givens(self) :
		items = [] # Financial_guarantees_given[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Financial_guarantees_givens = []
		self.Financial_guarantees_givens.extend(self.calc_Financial_guarantees_givens())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_18_00_e_REF_FINREP_3_0_Off_balance_sheet_exposures_subject_to_credit_risk_Table:
	Off_balance_sheet_exposures_subject_to_credit_risks = []# Off_balance_sheet_exposures_subject_to_credit_risk[]
	def calc_Off_balance_sheet_exposures_subject_to_credit_risks(self) :
		items = [] # Off_balance_sheet_exposures_subject_to_credit_risk[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Off_balance_sheet_exposures_subject_to_credit_risks = []
		self.Off_balance_sheet_exposures_subject_to_credit_risks.extend(self.calc_Off_balance_sheet_exposures_subject_to_credit_risks())
		CSVConverter.persist_object_as_csv(self,True)
		return None


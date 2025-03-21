from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_10_00_REF_FINREP_3_0_UnionItem:
	base = None #F_10_00_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.TYP_RSK"})
	def TYP_RSK(self) -> str:
		''' return string from TYP_RSK enumeration '''
		return self.base.TYP_RSK()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.base.TYP_HDG()
	@lineage(dependencies={"base.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.base.NTNL_AMNT()

class F_10_00_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def TYP_RSK() -> str:
		''' return string from TYP_RSK enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def TYP_HDG() -> str:
		''' return string from TYP_HDG enumeration '''
		pass
	def NTNL_AMNT() -> int:
		pass

class F_10_00_REF_FINREP_3_0_UnionTable :
	F_10_00_REF_FINREP_3_0_UnionItems = [] # F_10_00_REF_FINREP_3_0_UnionItem []
	F_10_00_REF_FINREP_3_0_Derivatives_ETC_Table = None # Derivatives_ETC
	F_10_00_REF_FINREP_3_0_Derivatives_OTC_Table = None # Derivatives_OTC
	def calc_F_10_00_REF_FINREP_3_0_UnionItems(self) -> list[F_10_00_REF_FINREP_3_0_UnionItem] :
		items = [] # F_10_00_REF_FINREP_3_0_UnionItem []
		for item in self.F_10_00_REF_FINREP_3_0_Derivatives_ETC_Table.Derivatives_ETCs:
			newItem = F_10_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_10_00_REF_FINREP_3_0_Derivatives_OTC_Table.Derivatives_OTCs:
			newItem = F_10_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_10_00_REF_FINREP_3_0_UnionItems = []
		self.F_10_00_REF_FINREP_3_0_UnionItems.extend(self.calc_F_10_00_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Derivatives_ETC(F_10_00_REF_FINREP_3_0_Base):
	pass

class Derivatives_OTC(F_10_00_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.TYP_RSK"})
	def TYP_RSK(self):
		return self.INSTRMNT.TYP_RSK
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	@lineage(dependencies={"INSTRMNT.NTNL_AMNT"})
	def NTNL_AMNT(self):
		return self.INSTRMNT.NTNL_AMNT

class F_10_00_REF_FINREP_3_0_Derivatives_ETC_Table:
	Derivatives_ETCs = []# Derivatives_ETC[]
	def calc_Derivatives_ETCs(self) :
		items = [] # Derivatives_ETC[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Derivatives_ETCs = []
		self.Derivatives_ETCs.extend(self.calc_Derivatives_ETCs())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_10_00_REF_FINREP_3_0_Derivatives_OTC_Table:
	INSTRMNT_Table = None # INSTRMNT
	Derivatives_OTCs = []# Derivatives_OTC[]
	def calc_Derivatives_OTCs(self) :
		items = [] # Derivatives_OTC[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Derivatives_OTCs = []
		self.Derivatives_OTCs.extend(self.calc_Derivatives_OTCs())
		CSVConverter.persist_object_as_csv(self,True)
		return None


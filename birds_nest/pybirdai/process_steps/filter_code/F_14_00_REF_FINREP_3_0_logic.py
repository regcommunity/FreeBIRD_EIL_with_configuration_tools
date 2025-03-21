from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_14_00_REF_FINREP_3_0_UnionItem:
	base = None #F_14_00_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.ACCMLTD_CHNGS_FV"})
	def ACCMLTD_CHNGS_FV(self) -> int:
		return self.base.ACCMLTD_CHNGS_FV()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
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
	@lineage(dependencies={"base.FV_HRRCHY"})
	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.base.FV_HRRCHY()
	@lineage(dependencies={"base.FV"})
	def FV(self) -> int:
		return self.base.FV()
	@lineage(dependencies={"base.FV_CHNG"})
	def FV_CHNG(self) -> int:
		return self.base.FV_CHNG()

class F_14_00_REF_FINREP_3_0_Base:
	def ACCMLTD_CHNGS_FV() -> int:
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
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
	def FV_HRRCHY() -> str:
		''' return string from FV_HRRCHY enumeration '''
		pass
	def FV() -> int:
		pass
	def FV_CHNG() -> int:
		pass

class F_14_00_REF_FINREP_3_0_UnionTable :
	F_14_00_REF_FINREP_3_0_UnionItems = [] # F_14_00_REF_FINREP_3_0_UnionItem []
	F_14_00_REF_FINREP_3_0_Derivatives_ETC_Table = None # Derivatives_ETC
	F_14_00_REF_FINREP_3_0_Derivatives_OTC_Table = None # Derivatives_OTC
	F_14_00_REF_FINREP_3_0_Debt_securities_Table = None # Debt_securities
	F_14_00_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_14_00_REF_FINREP_3_0_Loans_and_advances_Table = None # Loans_and_advances
	F_14_00_REF_FINREP_3_0_Deposits_Table = None # Deposits
	def calc_F_14_00_REF_FINREP_3_0_UnionItems(self) -> list[F_14_00_REF_FINREP_3_0_UnionItem] :
		items = [] # F_14_00_REF_FINREP_3_0_UnionItem []
		for item in self.F_14_00_REF_FINREP_3_0_Derivatives_ETC_Table.Derivatives_ETCs:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_14_00_REF_FINREP_3_0_Derivatives_OTC_Table.Derivatives_OTCs:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_14_00_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_14_00_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_14_00_REF_FINREP_3_0_Loans_and_advances_Table.Loans_and_advancess:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_14_00_REF_FINREP_3_0_Deposits_Table.Depositss:
			newItem = F_14_00_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_14_00_REF_FINREP_3_0_UnionItems = []
		self.F_14_00_REF_FINREP_3_0_UnionItems.extend(self.calc_F_14_00_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Derivatives_ETC(F_14_00_REF_FINREP_3_0_Base):
	pass

class Derivatives_OTC(F_14_00_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT

class Debt_securities(F_14_00_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_CHNGS_FV"})
	def ACCMLTD_CHNGS_FV(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_CHNGS_FV
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.FV_CHNG"})
	def FV_CHNG(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.FV_CHNG
	pass

class Non_Negotiable_bonds(F_14_00_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_CHNGS_FV"})
	def ACCMLTD_CHNGS_FV(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCMLTD_CHNGS_FV
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.FV_CHNG"})
	def FV_CHNG(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.FV_CHNG
	pass

class Loans_and_advances(F_14_00_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	pass
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.FV"})
	def FV(self):
		return self.CLLTRL.FV

class Deposits(F_14_00_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_ORGN"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT

class F_14_00_REF_FINREP_3_0_Derivatives_ETC_Table:
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


class F_14_00_REF_FINREP_3_0_Derivatives_OTC_Table:
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


class F_14_00_REF_FINREP_3_0_Debt_securities_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	Debt_securitiess = []# Debt_securities[]
	def calc_Debt_securitiess(self) :
		items = [] # Debt_securities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess = []
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_14_00_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_14_00_REF_FINREP_3_0_Loans_and_advances_Table:
	INSTRMNT_Table = None # INSTRMNT
	CLLTRL_Table = None # CLLTRL
	Loans_and_advancess = []# Loans_and_advances[]
	def calc_Loans_and_advancess(self) :
		items = [] # Loans_and_advances[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Loans_and_advancess = []
		self.Loans_and_advancess.extend(self.calc_Loans_and_advancess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_14_00_REF_FINREP_3_0_Deposits_Table:
	INSTRMNT_Table = None # INSTRMNT
	Depositss = []# Deposits[]
	def calc_Depositss(self) :
		items = [] # Deposits[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Depositss = []
		self.Depositss.extend(self.calc_Depositss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


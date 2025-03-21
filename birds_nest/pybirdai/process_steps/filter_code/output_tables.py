from pybirdai.process_steps.pybird.orchestration import Orchestration
from datetime import datetime
from pybirdai.annotations.decorators import lineage
from .F_01_01_REF_FINREP_3_0_logic import *

class F_01_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_01_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_01_01_REF_FINREP_3_0_Table :
	F_01_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_01_01_REF_FINREP_3_0s = [] #F_01_01_REF_FINREP_3_0[]
	def  calc_F_01_01_REF_FINREP_3_0s(self) -> list[F_01_01_REF_FINREP_3_0] :
		items = [] # F_01_01_REF_FINREP_3_0[]
		for item in self.F_01_01_REF_FINREP_3_0_UnionTable.F_01_01_REF_FINREP_3_0_UnionItems:
			newItem = F_01_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_01_01_REF_FINREP_3_0s = []
		self.F_01_01_REF_FINREP_3_0s.extend(self.calc_F_01_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_01_02_REF_FINREP_3_0_logic import *

class F_01_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_01_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_01_02_REF_FINREP_3_0_Table :
	F_01_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_01_02_REF_FINREP_3_0s = [] #F_01_02_REF_FINREP_3_0[]
	def  calc_F_01_02_REF_FINREP_3_0s(self) -> list[F_01_02_REF_FINREP_3_0] :
		items = [] # F_01_02_REF_FINREP_3_0[]
		for item in self.F_01_02_REF_FINREP_3_0_UnionTable.F_01_02_REF_FINREP_3_0_UnionItems:
			newItem = F_01_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_01_02_REF_FINREP_3_0s = []
		self.F_01_02_REF_FINREP_3_0s.extend(self.calc_F_01_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_01_REF_FINREP_3_0_logic import *

class F_04_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_04_01_REF_FINREP_3_0_Table :
	F_04_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_01_REF_FINREP_3_0s = [] #F_04_01_REF_FINREP_3_0[]
	def  calc_F_04_01_REF_FINREP_3_0s(self) -> list[F_04_01_REF_FINREP_3_0] :
		items = [] # F_04_01_REF_FINREP_3_0[]
		for item in self.F_04_01_REF_FINREP_3_0_UnionTable.F_04_01_REF_FINREP_3_0_UnionItems:
			newItem = F_04_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.F_04_01_REF_FINREP_3_0s.extend(self.calc_F_04_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_02_1_REF_FINREP_3_0_logic import *

class F_04_02_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_02_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_04_02_1_REF_FINREP_3_0_Table :
	F_04_02_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_02_1_REF_FINREP_3_0s = [] #F_04_02_1_REF_FINREP_3_0[]
	def  calc_F_04_02_1_REF_FINREP_3_0s(self) -> list[F_04_02_1_REF_FINREP_3_0] :
		items = [] # F_04_02_1_REF_FINREP_3_0[]
		for item in self.F_04_02_1_REF_FINREP_3_0_UnionTable.F_04_02_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_02_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_02_1_REF_FINREP_3_0s = []
		self.F_04_02_1_REF_FINREP_3_0s.extend(self.calc_F_04_02_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_02_2_REF_FINREP_3_0_logic import *

class F_04_02_2_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_02_2_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_04_02_2_REF_FINREP_3_0_Table :
	F_04_02_2_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_02_2_REF_FINREP_3_0s = [] #F_04_02_2_REF_FINREP_3_0[]
	def  calc_F_04_02_2_REF_FINREP_3_0s(self) -> list[F_04_02_2_REF_FINREP_3_0] :
		items = [] # F_04_02_2_REF_FINREP_3_0[]
		for item in self.F_04_02_2_REF_FINREP_3_0_UnionTable.F_04_02_2_REF_FINREP_3_0_UnionItems:
			newItem = F_04_02_2_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_02_2_REF_FINREP_3_0s = []
		self.F_04_02_2_REF_FINREP_3_0s.extend(self.calc_F_04_02_2_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_03_1_REF_FINREP_3_0_logic import *

class F_04_03_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_03_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_TTL_WRTFFS"})
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_PRTL_WRTFFS"})
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.LW_CRDT_RSK_INDCTR"})
	def LW_CRDT_RSK_INDCTR(self) -> str:
		''' return string from LW_CRDT_RSK_INDCTR enumeration '''
		return self.unionOfLayers.LW_CRDT_RSK_INDCTR()


class F_04_03_1_REF_FINREP_3_0_Table :
	F_04_03_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_03_1_REF_FINREP_3_0s = [] #F_04_03_1_REF_FINREP_3_0[]
	def  calc_F_04_03_1_REF_FINREP_3_0s(self) -> list[F_04_03_1_REF_FINREP_3_0] :
		items = [] # F_04_03_1_REF_FINREP_3_0[]
		for item in self.F_04_03_1_REF_FINREP_3_0_UnionTable.F_04_03_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_03_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_03_1_REF_FINREP_3_0s = []
		self.F_04_03_1_REF_FINREP_3_0s.extend(self.calc_F_04_03_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_04_1_REF_FINREP_3_0_logic import *

class F_04_04_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_04_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_PRTL_WRTFFS"})
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_TTL_WRTFFS"})
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.LW_CRDT_RSK_INDCTR"})
	def LW_CRDT_RSK_INDCTR(self) -> str:
		''' return string from LW_CRDT_RSK_INDCTR enumeration '''
		return self.unionOfLayers.LW_CRDT_RSK_INDCTR()


class F_04_04_1_REF_FINREP_3_0_Table :
	F_04_04_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_04_1_REF_FINREP_3_0s = [] #F_04_04_1_REF_FINREP_3_0[]
	def  calc_F_04_04_1_REF_FINREP_3_0s(self) -> list[F_04_04_1_REF_FINREP_3_0] :
		items = [] # F_04_04_1_REF_FINREP_3_0[]
		for item in self.F_04_04_1_REF_FINREP_3_0_UnionTable.F_04_04_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_04_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_04_1_REF_FINREP_3_0s = []
		self.F_04_04_1_REF_FINREP_3_0s.extend(self.calc_F_04_04_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_05_REF_FINREP_3_0_logic import *

class F_04_05_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_05_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.SBRDNTD_DBT"})
	def SBRDNTD_DBT(self) -> str:
		''' return string from SBRDNTD_DBT enumeration '''
		return self.unionOfLayers.SBRDNTD_DBT()


class F_04_05_REF_FINREP_3_0_Table :
	F_04_05_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_05_REF_FINREP_3_0s = [] #F_04_05_REF_FINREP_3_0[]
	def  calc_F_04_05_REF_FINREP_3_0s(self) -> list[F_04_05_REF_FINREP_3_0] :
		items = [] # F_04_05_REF_FINREP_3_0[]
		for item in self.F_04_05_REF_FINREP_3_0_UnionTable.F_04_05_REF_FINREP_3_0_UnionItems:
			newItem = F_04_05_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_05_REF_FINREP_3_0s = []
		self.F_04_05_REF_FINREP_3_0s.extend(self.calc_F_04_05_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_06_REF_FINREP_3_0_logic import *

class F_04_06_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_06_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_04_06_REF_FINREP_3_0_Table :
	F_04_06_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_06_REF_FINREP_3_0s = [] #F_04_06_REF_FINREP_3_0[]
	def  calc_F_04_06_REF_FINREP_3_0s(self) -> list[F_04_06_REF_FINREP_3_0] :
		items = [] # F_04_06_REF_FINREP_3_0[]
		for item in self.F_04_06_REF_FINREP_3_0_UnionTable.F_04_06_REF_FINREP_3_0_UnionItems:
			newItem = F_04_06_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_06_REF_FINREP_3_0s = []
		self.F_04_06_REF_FINREP_3_0s.extend(self.calc_F_04_06_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_07_REF_FINREP_3_0_logic import *

class F_04_07_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_07_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()


class F_04_07_REF_FINREP_3_0_Table :
	F_04_07_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_07_REF_FINREP_3_0s = [] #F_04_07_REF_FINREP_3_0[]
	def  calc_F_04_07_REF_FINREP_3_0s(self) -> list[F_04_07_REF_FINREP_3_0] :
		items = [] # F_04_07_REF_FINREP_3_0[]
		for item in self.F_04_07_REF_FINREP_3_0_UnionTable.F_04_07_REF_FINREP_3_0_UnionItems:
			newItem = F_04_07_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_07_REF_FINREP_3_0s = []
		self.F_04_07_REF_FINREP_3_0s.extend(self.calc_F_04_07_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_08_REF_FINREP_3_0_logic import *

class F_04_08_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_08_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_TTL_WRTFFS"})
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_PRTL_WRTFFS"})
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_08_REF_FINREP_3_0_Table :
	F_04_08_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_08_REF_FINREP_3_0s = [] #F_04_08_REF_FINREP_3_0[]
	def  calc_F_04_08_REF_FINREP_3_0s(self) -> list[F_04_08_REF_FINREP_3_0] :
		items = [] # F_04_08_REF_FINREP_3_0[]
		for item in self.F_04_08_REF_FINREP_3_0_UnionTable.F_04_08_REF_FINREP_3_0_UnionItems:
			newItem = F_04_08_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_08_REF_FINREP_3_0s = []
		self.F_04_08_REF_FINREP_3_0s.extend(self.calc_F_04_08_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_09_REF_FINREP_3_0_logic import *

class F_04_09_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_09_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR"})
	def ACCMLTD_NGTV_VL_ADJSTMNT_MR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_PRTL_WRTFFS"})
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_TTL_WRTFFS"})
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_CR"})
	def ACCMLTD_NGTV_VL_ADJSTMNT_CR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_CR()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_09_REF_FINREP_3_0_Table :
	F_04_09_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_09_REF_FINREP_3_0s = [] #F_04_09_REF_FINREP_3_0[]
	def  calc_F_04_09_REF_FINREP_3_0s(self) -> list[F_04_09_REF_FINREP_3_0] :
		items = [] # F_04_09_REF_FINREP_3_0[]
		for item in self.F_04_09_REF_FINREP_3_0_UnionTable.F_04_09_REF_FINREP_3_0_UnionItems:
			newItem = F_04_09_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_09_REF_FINREP_3_0s = []
		self.F_04_09_REF_FINREP_3_0s.extend(self.calc_F_04_09_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_10_REF_FINREP_3_0_logic import *

class F_04_10_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_10_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_PRTL_WRTFFS"})
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_CR"})
	def ACCMLTD_NGTV_VL_ADJSTMNT_CR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_CR()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR"})
	def ACCMLTD_NGTV_VL_ADJSTMNT_MR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_TTL_WRTFFS"})
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_10_REF_FINREP_3_0_Table :
	F_04_10_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_10_REF_FINREP_3_0s = [] #F_04_10_REF_FINREP_3_0[]
	def  calc_F_04_10_REF_FINREP_3_0s(self) -> list[F_04_10_REF_FINREP_3_0] :
		items = [] # F_04_10_REF_FINREP_3_0[]
		for item in self.F_04_10_REF_FINREP_3_0_UnionTable.F_04_10_REF_FINREP_3_0_UnionItems:
			newItem = F_04_10_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_10_REF_FINREP_3_0s = []
		self.F_04_10_REF_FINREP_3_0s.extend(self.calc_F_04_10_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_05_01_REF_FINREP_3_0_logic import *

class F_05_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_05_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_05_01_REF_FINREP_3_0_Table :
	F_05_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_05_01_REF_FINREP_3_0s = [] #F_05_01_REF_FINREP_3_0[]
	def  calc_F_05_01_REF_FINREP_3_0s(self) -> list[F_05_01_REF_FINREP_3_0] :
		items = [] # F_05_01_REF_FINREP_3_0[]
		for item in self.F_05_01_REF_FINREP_3_0_UnionTable.F_05_01_REF_FINREP_3_0_UnionItems:
			newItem = F_05_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.F_05_01_REF_FINREP_3_0s.extend(self.calc_F_05_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_06_01_REF_FINREP_3_0_logic import *

class F_06_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_06_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ECNMC_ACTVTY"})
	def ECNMC_ACTVTY(self) -> str:
		''' return string from ECNMC_ACTVTY enumeration '''
		return self.unionOfLayers.ECNMC_ACTVTY()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()


class F_06_01_REF_FINREP_3_0_Table :
	F_06_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_06_01_REF_FINREP_3_0s = [] #F_06_01_REF_FINREP_3_0[]
	def  calc_F_06_01_REF_FINREP_3_0s(self) -> list[F_06_01_REF_FINREP_3_0] :
		items = [] # F_06_01_REF_FINREP_3_0[]
		for item in self.F_06_01_REF_FINREP_3_0_UnionTable.F_06_01_REF_FINREP_3_0_UnionItems:
			newItem = F_06_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_06_01_REF_FINREP_3_0s = []
		self.F_06_01_REF_FINREP_3_0s.extend(self.calc_F_06_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_07_01_REF_FINREP_3_0_logic import *

class F_07_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_07_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()


class F_07_01_REF_FINREP_3_0_Table :
	F_07_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_07_01_REF_FINREP_3_0s = [] #F_07_01_REF_FINREP_3_0[]
	def  calc_F_07_01_REF_FINREP_3_0s(self) -> list[F_07_01_REF_FINREP_3_0] :
		items = [] # F_07_01_REF_FINREP_3_0[]
		for item in self.F_07_01_REF_FINREP_3_0_UnionTable.F_07_01_REF_FINREP_3_0_UnionItems:
			newItem = F_07_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_07_01_REF_FINREP_3_0s = []
		self.F_07_01_REF_FINREP_3_0s.extend(self.calc_F_07_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_07_02_REF_FINREP_3_0_logic import *

class F_07_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_07_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()


class F_07_02_REF_FINREP_3_0_Table :
	F_07_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_07_02_REF_FINREP_3_0s = [] #F_07_02_REF_FINREP_3_0[]
	def  calc_F_07_02_REF_FINREP_3_0s(self) -> list[F_07_02_REF_FINREP_3_0] :
		items = [] # F_07_02_REF_FINREP_3_0[]
		for item in self.F_07_02_REF_FINREP_3_0_UnionTable.F_07_02_REF_FINREP_3_0_UnionItems:
			newItem = F_07_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_07_02_REF_FINREP_3_0s = []
		self.F_07_02_REF_FINREP_3_0s.extend(self.calc_F_07_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_08_01_a_REF_FINREP_3_0_logic import *

class F_08_01_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_08_01_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_CHNGS_FV_CR"})
	def ACCMLTD_CHNGS_FV_CR(self) -> int:
		return self.unionOfLayers.ACCMLTD_CHNGS_FV_CR()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_08_01_a_REF_FINREP_3_0_Table :
	F_08_01_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_08_01_a_REF_FINREP_3_0s = [] #F_08_01_a_REF_FINREP_3_0[]
	def  calc_F_08_01_a_REF_FINREP_3_0s(self) -> list[F_08_01_a_REF_FINREP_3_0] :
		items = [] # F_08_01_a_REF_FINREP_3_0[]
		for item in self.F_08_01_a_REF_FINREP_3_0_UnionTable.F_08_01_a_REF_FINREP_3_0_UnionItems:
			newItem = F_08_01_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_08_01_a_REF_FINREP_3_0s = []
		self.F_08_01_a_REF_FINREP_3_0s.extend(self.calc_F_08_01_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_08_02_REF_FINREP_3_0_logic import *

class F_08_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_08_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.SBRDNTD_DBT"})
	def SBRDNTD_DBT(self) -> str:
		''' return string from SBRDNTD_DBT enumeration '''
		return self.unionOfLayers.SBRDNTD_DBT()


class F_08_02_REF_FINREP_3_0_Table :
	F_08_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_08_02_REF_FINREP_3_0s = [] #F_08_02_REF_FINREP_3_0[]
	def  calc_F_08_02_REF_FINREP_3_0s(self) -> list[F_08_02_REF_FINREP_3_0] :
		items = [] # F_08_02_REF_FINREP_3_0[]
		for item in self.F_08_02_REF_FINREP_3_0_UnionTable.F_08_02_REF_FINREP_3_0_UnionItems:
			newItem = F_08_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_08_02_REF_FINREP_3_0s = []
		self.F_08_02_REF_FINREP_3_0s.extend(self.calc_F_08_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_09_01_REF_FINREP_3_0_logic import *

class F_09_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_09_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_09_01_REF_FINREP_3_0_Table :
	F_09_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_09_01_REF_FINREP_3_0s = [] #F_09_01_REF_FINREP_3_0[]
	def  calc_F_09_01_REF_FINREP_3_0s(self) -> list[F_09_01_REF_FINREP_3_0] :
		items = [] # F_09_01_REF_FINREP_3_0[]
		for item in self.F_09_01_REF_FINREP_3_0_UnionTable.F_09_01_REF_FINREP_3_0_UnionItems:
			newItem = F_09_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_09_01_REF_FINREP_3_0s = []
		self.F_09_01_REF_FINREP_3_0s.extend(self.calc_F_09_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_09_01_1_REF_FINREP_3_0_logic import *

class F_09_01_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_09_01_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_09_01_1_REF_FINREP_3_0_Table :
	F_09_01_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_09_01_1_REF_FINREP_3_0s = [] #F_09_01_1_REF_FINREP_3_0[]
	def  calc_F_09_01_1_REF_FINREP_3_0s(self) -> list[F_09_01_1_REF_FINREP_3_0] :
		items = [] # F_09_01_1_REF_FINREP_3_0[]
		for item in self.F_09_01_1_REF_FINREP_3_0_UnionTable.F_09_01_1_REF_FINREP_3_0_UnionItems:
			newItem = F_09_01_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_09_01_1_REF_FINREP_3_0s = []
		self.F_09_01_1_REF_FINREP_3_0s.extend(self.calc_F_09_01_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_10_00_REF_FINREP_3_0_logic import *

class F_10_00_REF_FINREP_3_0:
	unionOfLayers = None #  F_10_00_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_RSK"})
	def TYP_RSK(self) -> str:
		''' return string from TYP_RSK enumeration '''
		return self.unionOfLayers.TYP_RSK()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()

	@lineage(dependencies={"unionOfLayers.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.unionOfLayers.NTNL_AMNT()


class F_10_00_REF_FINREP_3_0_Table :
	F_10_00_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_10_00_REF_FINREP_3_0s = [] #F_10_00_REF_FINREP_3_0[]
	def  calc_F_10_00_REF_FINREP_3_0s(self) -> list[F_10_00_REF_FINREP_3_0] :
		items = [] # F_10_00_REF_FINREP_3_0[]
		for item in self.F_10_00_REF_FINREP_3_0_UnionTable.F_10_00_REF_FINREP_3_0_UnionItems:
			newItem = F_10_00_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_10_00_REF_FINREP_3_0s = []
		self.F_10_00_REF_FINREP_3_0s.extend(self.calc_F_10_00_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_11_01_REF_FINREP_3_0_logic import *

class F_11_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_11_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.unionOfLayers.NTNL_AMNT()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_RSK"})
	def TYP_RSK(self) -> str:
		''' return string from TYP_RSK enumeration '''
		return self.unionOfLayers.TYP_RSK()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_11_01_REF_FINREP_3_0_Table :
	F_11_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_11_01_REF_FINREP_3_0s = [] #F_11_01_REF_FINREP_3_0[]
	def  calc_F_11_01_REF_FINREP_3_0s(self) -> list[F_11_01_REF_FINREP_3_0] :
		items = [] # F_11_01_REF_FINREP_3_0[]
		for item in self.F_11_01_REF_FINREP_3_0_UnionTable.F_11_01_REF_FINREP_3_0_UnionItems:
			newItem = F_11_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_11_01_REF_FINREP_3_0s = []
		self.F_11_01_REF_FINREP_3_0s.extend(self.calc_F_11_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_11_02_REF_FINREP_3_0_logic import *

class F_11_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_11_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_RSK"})
	def TYP_RSK(self) -> str:
		''' return string from TYP_RSK enumeration '''
		return self.unionOfLayers.TYP_RSK()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()

	@lineage(dependencies={"unionOfLayers.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.unionOfLayers.NTNL_AMNT()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_11_02_REF_FINREP_3_0_Table :
	F_11_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_11_02_REF_FINREP_3_0s = [] #F_11_02_REF_FINREP_3_0[]
	def  calc_F_11_02_REF_FINREP_3_0s(self) -> list[F_11_02_REF_FINREP_3_0] :
		items = [] # F_11_02_REF_FINREP_3_0[]
		for item in self.F_11_02_REF_FINREP_3_0_UnionTable.F_11_02_REF_FINREP_3_0_UnionItems:
			newItem = F_11_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_11_02_REF_FINREP_3_0s = []
		self.F_11_02_REF_FINREP_3_0s.extend(self.calc_F_11_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_13_01_REF_FINREP_3_0_logic import *

class F_13_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_13_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_13_01_REF_FINREP_3_0_Table :
	F_13_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_13_01_REF_FINREP_3_0s = [] #F_13_01_REF_FINREP_3_0[]
	def  calc_F_13_01_REF_FINREP_3_0s(self) -> list[F_13_01_REF_FINREP_3_0] :
		items = [] # F_13_01_REF_FINREP_3_0[]
		for item in self.F_13_01_REF_FINREP_3_0_UnionTable.F_13_01_REF_FINREP_3_0_UnionItems:
			newItem = F_13_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_13_01_REF_FINREP_3_0s = []
		self.F_13_01_REF_FINREP_3_0s.extend(self.calc_F_13_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_14_00_REF_FINREP_3_0_logic import *

class F_14_00_REF_FINREP_3_0:
	unionOfLayers = None #  F_14_00_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_CHNGS_FV"})
	def ACCMLTD_CHNGS_FV(self) -> int:
		return self.unionOfLayers.ACCMLTD_CHNGS_FV()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.FV_HRRCHY"})
	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.unionOfLayers.FV_HRRCHY()

	@lineage(dependencies={"unionOfLayers.FV"})
	def FV(self) -> int:
		return self.unionOfLayers.FV()

	@lineage(dependencies={"unionOfLayers.FV_CHNG"})
	def FV_CHNG(self) -> int:
		return self.unionOfLayers.FV_CHNG()


class F_14_00_REF_FINREP_3_0_Table :
	F_14_00_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_14_00_REF_FINREP_3_0s = [] #F_14_00_REF_FINREP_3_0[]
	def  calc_F_14_00_REF_FINREP_3_0s(self) -> list[F_14_00_REF_FINREP_3_0] :
		items = [] # F_14_00_REF_FINREP_3_0[]
		for item in self.F_14_00_REF_FINREP_3_0_UnionTable.F_14_00_REF_FINREP_3_0_UnionItems:
			newItem = F_14_00_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_14_00_REF_FINREP_3_0s = []
		self.F_14_00_REF_FINREP_3_0s.extend(self.calc_F_14_00_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_15_00_a_REF_FINREP_3_0_logic import *

class F_15_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_15_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT"})
	def TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT(self) -> str:
		''' return string from RCGNTN_STTS enumeration '''
		return self.unionOfLayers.TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.AMNT_DRCGNSD_CPTL_PRPS"})
	def AMNT_DRCGNSD_CPTL_PRPS(self) -> int:
		return self.unionOfLayers.AMNT_DRCGNSD_CPTL_PRPS()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_15_00_a_REF_FINREP_3_0_Table :
	F_15_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_15_00_a_REF_FINREP_3_0s = [] #F_15_00_a_REF_FINREP_3_0[]
	def  calc_F_15_00_a_REF_FINREP_3_0s(self) -> list[F_15_00_a_REF_FINREP_3_0] :
		items = [] # F_15_00_a_REF_FINREP_3_0[]
		for item in self.F_15_00_a_REF_FINREP_3_0_UnionTable.F_15_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_15_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_15_00_a_REF_FINREP_3_0s = []
		self.F_15_00_a_REF_FINREP_3_0s.extend(self.calc_F_15_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_a_REF_FINREP_3_0_logic import *

class F_18_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_18_00_a_REF_FINREP_3_0_Table :
	F_18_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_a_REF_FINREP_3_0s = [] #F_18_00_a_REF_FINREP_3_0[]
	def  calc_F_18_00_a_REF_FINREP_3_0s(self) -> list[F_18_00_a_REF_FINREP_3_0] :
		items = [] # F_18_00_a_REF_FINREP_3_0[]
		for item in self.F_18_00_a_REF_FINREP_3_0_UnionTable.F_18_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_a_REF_FINREP_3_0s = []
		self.F_18_00_a_REF_FINREP_3_0s.extend(self.calc_F_18_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_b_REF_FINREP_3_0_logic import *

class F_18_00_b_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_b_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()


class F_18_00_b_REF_FINREP_3_0_Table :
	F_18_00_b_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_b_REF_FINREP_3_0s = [] #F_18_00_b_REF_FINREP_3_0[]
	def  calc_F_18_00_b_REF_FINREP_3_0s(self) -> list[F_18_00_b_REF_FINREP_3_0] :
		items = [] # F_18_00_b_REF_FINREP_3_0[]
		for item in self.F_18_00_b_REF_FINREP_3_0_UnionTable.F_18_00_b_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_b_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_b_REF_FINREP_3_0s = []
		self.F_18_00_b_REF_FINREP_3_0s.extend(self.calc_F_18_00_b_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_c_REF_FINREP_3_0_logic import *

class F_18_00_c_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_c_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_18_00_c_REF_FINREP_3_0_Table :
	F_18_00_c_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_c_REF_FINREP_3_0s = [] #F_18_00_c_REF_FINREP_3_0[]
	def  calc_F_18_00_c_REF_FINREP_3_0s(self) -> list[F_18_00_c_REF_FINREP_3_0] :
		items = [] # F_18_00_c_REF_FINREP_3_0[]
		for item in self.F_18_00_c_REF_FINREP_3_0_UnionTable.F_18_00_c_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_c_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_c_REF_FINREP_3_0s = []
		self.F_18_00_c_REF_FINREP_3_0s.extend(self.calc_F_18_00_c_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_d_REF_FINREP_3_0_logic import *

class F_18_00_d_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_d_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_18_00_d_REF_FINREP_3_0_Table :
	F_18_00_d_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_d_REF_FINREP_3_0s = [] #F_18_00_d_REF_FINREP_3_0[]
	def  calc_F_18_00_d_REF_FINREP_3_0s(self) -> list[F_18_00_d_REF_FINREP_3_0] :
		items = [] # F_18_00_d_REF_FINREP_3_0[]
		for item in self.F_18_00_d_REF_FINREP_3_0_UnionTable.F_18_00_d_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_d_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_d_REF_FINREP_3_0s = []
		self.F_18_00_d_REF_FINREP_3_0s.extend(self.calc_F_18_00_d_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_e_REF_FINREP_3_0_logic import *

class F_18_00_e_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_e_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_18_00_e_REF_FINREP_3_0_Table :
	F_18_00_e_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_e_REF_FINREP_3_0s = [] #F_18_00_e_REF_FINREP_3_0[]
	def  calc_F_18_00_e_REF_FINREP_3_0s(self) -> list[F_18_00_e_REF_FINREP_3_0] :
		items = [] # F_18_00_e_REF_FINREP_3_0[]
		for item in self.F_18_00_e_REF_FINREP_3_0_UnionTable.F_18_00_e_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_e_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_e_REF_FINREP_3_0s = []
		self.F_18_00_e_REF_FINREP_3_0s.extend(self.calc_F_18_00_e_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_a_REF_FINREP_3_0_logic import *

class F_19_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.IMPRMNT_STTS"})
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.NN_PRFRMNG_PRR_FRBRNC_INDCTR"})
	def NN_PRFRMNG_PRR_FRBRNC_INDCTR(self) -> str:
		''' return string from NN_PRFRMNG_PRR_FRBRNC_INDCTR enumeration '''
		return self.unionOfLayers.NN_PRFRMNG_PRR_FRBRNC_INDCTR()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS_RSN"})
	def PRFRMNG_STTS_RSN(self) -> str:
		''' return string from PRFRMNG_STTS_RSN enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS_RSN()


class F_19_00_a_REF_FINREP_3_0_Table :
	F_19_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_a_REF_FINREP_3_0s = [] #F_19_00_a_REF_FINREP_3_0[]
	def  calc_F_19_00_a_REF_FINREP_3_0s(self) -> list[F_19_00_a_REF_FINREP_3_0] :
		items = [] # F_19_00_a_REF_FINREP_3_0[]
		for item in self.F_19_00_a_REF_FINREP_3_0_UnionTable.F_19_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_a_REF_FINREP_3_0s = []
		self.F_19_00_a_REF_FINREP_3_0s.extend(self.calc_F_19_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_b_REF_FINREP_3_0_logic import *

class F_19_00_b_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_b_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_19_00_b_REF_FINREP_3_0_Table :
	F_19_00_b_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_b_REF_FINREP_3_0s = [] #F_19_00_b_REF_FINREP_3_0[]
	def  calc_F_19_00_b_REF_FINREP_3_0s(self) -> list[F_19_00_b_REF_FINREP_3_0] :
		items = [] # F_19_00_b_REF_FINREP_3_0[]
		for item in self.F_19_00_b_REF_FINREP_3_0_UnionTable.F_19_00_b_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_b_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_b_REF_FINREP_3_0s = []
		self.F_19_00_b_REF_FINREP_3_0s.extend(self.calc_F_19_00_b_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_c_REF_FINREP_3_0_logic import *

class F_19_00_c_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_c_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_19_00_c_REF_FINREP_3_0_Table :
	F_19_00_c_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_c_REF_FINREP_3_0s = [] #F_19_00_c_REF_FINREP_3_0[]
	def  calc_F_19_00_c_REF_FINREP_3_0s(self) -> list[F_19_00_c_REF_FINREP_3_0] :
		items = [] # F_19_00_c_REF_FINREP_3_0[]
		for item in self.F_19_00_c_REF_FINREP_3_0_UnionTable.F_19_00_c_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_c_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_c_REF_FINREP_3_0s = []
		self.F_19_00_c_REF_FINREP_3_0s.extend(self.calc_F_19_00_c_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_e_REF_FINREP_3_0_logic import *

class F_19_00_e_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_e_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()


class F_19_00_e_REF_FINREP_3_0_Table :
	F_19_00_e_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_e_REF_FINREP_3_0s = [] #F_19_00_e_REF_FINREP_3_0[]
	def  calc_F_19_00_e_REF_FINREP_3_0s(self) -> list[F_19_00_e_REF_FINREP_3_0] :
		items = [] # F_19_00_e_REF_FINREP_3_0[]
		for item in self.F_19_00_e_REF_FINREP_3_0_UnionTable.F_19_00_e_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_e_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_e_REF_FINREP_3_0s = []
		self.F_19_00_e_REF_FINREP_3_0s.extend(self.calc_F_19_00_e_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_01_REF_FINREP_3_0_logic import *

class F_20_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_20_01_REF_FINREP_3_0_Table :
	F_20_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_01_REF_FINREP_3_0s = [] #F_20_01_REF_FINREP_3_0[]
	def  calc_F_20_01_REF_FINREP_3_0s(self) -> list[F_20_01_REF_FINREP_3_0] :
		items = [] # F_20_01_REF_FINREP_3_0[]
		for item in self.F_20_01_REF_FINREP_3_0_UnionTable.F_20_01_REF_FINREP_3_0_UnionItems:
			newItem = F_20_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_01_REF_FINREP_3_0s = []
		self.F_20_01_REF_FINREP_3_0s.extend(self.calc_F_20_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_02_REF_FINREP_3_0_logic import *

class F_20_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_20_02_REF_FINREP_3_0_Table :
	F_20_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_02_REF_FINREP_3_0s = [] #F_20_02_REF_FINREP_3_0[]
	def  calc_F_20_02_REF_FINREP_3_0s(self) -> list[F_20_02_REF_FINREP_3_0] :
		items = [] # F_20_02_REF_FINREP_3_0[]
		for item in self.F_20_02_REF_FINREP_3_0_UnionTable.F_20_02_REF_FINREP_3_0_UnionItems:
			newItem = F_20_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_02_REF_FINREP_3_0s = []
		self.F_20_02_REF_FINREP_3_0s.extend(self.calc_F_20_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_04_REF_FINREP_3_0_logic import *

class F_20_04_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_04_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ENTRPRS_SZ"})
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_20_04_REF_FINREP_3_0_Table :
	F_20_04_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_04_REF_FINREP_3_0s = [] #F_20_04_REF_FINREP_3_0[]
	def  calc_F_20_04_REF_FINREP_3_0s(self) -> list[F_20_04_REF_FINREP_3_0] :
		items = [] # F_20_04_REF_FINREP_3_0[]
		for item in self.F_20_04_REF_FINREP_3_0_UnionTable.F_20_04_REF_FINREP_3_0_UnionItems:
			newItem = F_20_04_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_04_REF_FINREP_3_0s = []
		self.F_20_04_REF_FINREP_3_0s.extend(self.calc_F_20_04_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_05_a_REF_FINREP_3_0_logic import *

class F_20_05_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_05_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	@lineage(dependencies={"unionOfLayers.DFLT_STTS"})
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()


class F_20_05_a_REF_FINREP_3_0_Table :
	F_20_05_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_05_a_REF_FINREP_3_0s = [] #F_20_05_a_REF_FINREP_3_0[]
	def  calc_F_20_05_a_REF_FINREP_3_0s(self) -> list[F_20_05_a_REF_FINREP_3_0] :
		items = [] # F_20_05_a_REF_FINREP_3_0[]
		for item in self.F_20_05_a_REF_FINREP_3_0_UnionTable.F_20_05_a_REF_FINREP_3_0_UnionItems:
			newItem = F_20_05_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_05_a_REF_FINREP_3_0s = []
		self.F_20_05_a_REF_FINREP_3_0s.extend(self.calc_F_20_05_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_06_REF_FINREP_3_0_logic import *

class F_20_06_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_06_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_20_06_REF_FINREP_3_0_Table :
	F_20_06_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_06_REF_FINREP_3_0s = [] #F_20_06_REF_FINREP_3_0[]
	def  calc_F_20_06_REF_FINREP_3_0s(self) -> list[F_20_06_REF_FINREP_3_0] :
		items = [] # F_20_06_REF_FINREP_3_0[]
		for item in self.F_20_06_REF_FINREP_3_0_UnionTable.F_20_06_REF_FINREP_3_0_UnionItems:
			newItem = F_20_06_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_06_REF_FINREP_3_0s = []
		self.F_20_06_REF_FINREP_3_0s.extend(self.calc_F_20_06_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_07_1_REF_FINREP_3_0_logic import *

class F_20_07_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_07_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ECNMC_ACTVTY"})
	def ECNMC_ACTVTY(self) -> str:
		''' return string from ECNMC_ACTVTY enumeration '''
		return self.unionOfLayers.ECNMC_ACTVTY()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	@lineage(dependencies={"unionOfLayers.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_20_07_1_REF_FINREP_3_0_Table :
	F_20_07_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_07_1_REF_FINREP_3_0s = [] #F_20_07_1_REF_FINREP_3_0[]
	def  calc_F_20_07_1_REF_FINREP_3_0s(self) -> list[F_20_07_1_REF_FINREP_3_0] :
		items = [] # F_20_07_1_REF_FINREP_3_0[]
		for item in self.F_20_07_1_REF_FINREP_3_0_UnionTable.F_20_07_1_REF_FINREP_3_0_UnionItems:
			newItem = F_20_07_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_07_1_REF_FINREP_3_0s = []
		self.F_20_07_1_REF_FINREP_3_0s.extend(self.calc_F_20_07_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_31_01_REF_FINREP_3_0_logic import *

class F_31_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_31_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PRFRMNG_STTS"})
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	@lineage(dependencies={"unionOfLayers.NMNL_AMNT"})
	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	@lineage(dependencies={"unionOfLayers.NTNL_AMNT"})
	def NTNL_AMNT(self) -> int:
		return self.unionOfLayers.NTNL_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCMLTD_IMPRMNT"})
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()


class F_31_01_REF_FINREP_3_0_Table :
	F_31_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_31_01_REF_FINREP_3_0s = [] #F_31_01_REF_FINREP_3_0[]
	def  calc_F_31_01_REF_FINREP_3_0s(self) -> list[F_31_01_REF_FINREP_3_0] :
		items = [] # F_31_01_REF_FINREP_3_0[]
		for item in self.F_31_01_REF_FINREP_3_0_UnionTable.F_31_01_REF_FINREP_3_0_UnionItems:
			newItem = F_31_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_31_01_REF_FINREP_3_0s = []
		self.F_31_01_REF_FINREP_3_0s.extend(self.calc_F_31_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_41_01_REF_FINREP_3_0_logic import *

class F_41_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_41_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.FV"})
	def FV(self) -> int:
		return self.unionOfLayers.FV()

	@lineage(dependencies={"unionOfLayers.FV_HRRCHY"})
	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.unionOfLayers.FV_HRRCHY()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()


class F_41_01_REF_FINREP_3_0_Table :
	F_41_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_41_01_REF_FINREP_3_0s = [] #F_41_01_REF_FINREP_3_0[]
	def  calc_F_41_01_REF_FINREP_3_0s(self) -> list[F_41_01_REF_FINREP_3_0] :
		items = [] # F_41_01_REF_FINREP_3_0[]
		for item in self.F_41_01_REF_FINREP_3_0_UnionTable.F_41_01_REF_FINREP_3_0_UnionItems:
			newItem = F_41_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_41_01_REF_FINREP_3_0s = []
		self.F_41_01_REF_FINREP_3_0s.extend(self.calc_F_41_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_41_02_REF_FINREP_3_0_logic import *

class F_41_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_41_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	@lineage(dependencies={"unionOfLayers.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	@lineage(dependencies={"unionOfLayers.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	@lineage(dependencies={"unionOfLayers.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.FVO_DSGNTN"})
	def FVO_DSGNTN(self) -> str:
		''' return string from FVO_DSGNTN enumeration '''
		return self.unionOfLayers.FVO_DSGNTN()


class F_41_02_REF_FINREP_3_0_Table :
	F_41_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_41_02_REF_FINREP_3_0s = [] #F_41_02_REF_FINREP_3_0[]
	def  calc_F_41_02_REF_FINREP_3_0s(self) -> list[F_41_02_REF_FINREP_3_0] :
		items = [] # F_41_02_REF_FINREP_3_0[]
		for item in self.F_41_02_REF_FINREP_3_0_UnionTable.F_41_02_REF_FINREP_3_0_UnionItems:
			newItem = F_41_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_41_02_REF_FINREP_3_0s = []
		self.F_41_02_REF_FINREP_3_0s.extend(self.calc_F_41_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None


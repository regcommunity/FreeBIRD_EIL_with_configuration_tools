from pybirdai.process_steps.pybird.orchestration import Orchestration
from datetime import datetime
from pybirdai.annotations.decorators import lineage
from .ANCRDT_INSTRMNT_C_1_logic import *

class ANCRDT_INSTRMNT_C_1:
	unionOfLayers = None #  ANCRDT_INSTRMNT_C_1_UnionItem  unionOfLayers
	@lineage(dependencies={"unionOfLayers.RCRS"})
	def RCRS(self) -> str:
		''' return string from RCRS enumeration '''
		return self.unionOfLayers.RCRS()

	@lineage(dependencies={"unionOfLayers.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	@lineage(dependencies={"unionOfLayers.FDCRY"})
	def FDCRY(self) -> str:
		''' return string from FDCRY enumeration '''
		return self.unionOfLayers.FDCRY()

	@lineage(dependencies={"unionOfLayers.RFRNC_RT"})
	def RFRNC_RT(self) -> str:
		''' return string from RFRNC_RT enumeration '''
		return self.unionOfLayers.RFRNC_RT()

	@lineage(dependencies={"unionOfLayers.DT_RFRNC"})
	def DT_RFRNC(self) -> datetime:
		return self.unionOfLayers.DT_RFRNC()

	@lineage(dependencies={"unionOfLayers.CNTRCT_ID"})
	def CNTRCT_ID(self) -> str:
		''' return string from STRNG enumeration '''
		return self.unionOfLayers.CNTRCT_ID()

	@lineage(dependencies={"unionOfLayers.DT_INCPTN"})
	def DT_INCPTN(self) -> datetime:
		return self.unionOfLayers.DT_INCPTN()

	@lineage(dependencies={"unionOfLayers.DT_STTLMNT"})
	def DT_STTLMNT(self) -> datetime:
		return self.unionOfLayers.DT_STTLMNT()

	@lineage(dependencies={"unionOfLayers.TYP_AMRTSTN"})
	def TYP_AMRTSTN(self) -> str:
		''' return string from TYP_AMRTSTN enumeration '''
		return self.unionOfLayers.TYP_AMRTSTN()

	@lineage(dependencies={"unionOfLayers.INSTRMNT_ID"})
	def INSTRMNT_ID(self) -> str:
		return self.unionOfLayers.INSTRMNT_ID()

	@lineage(dependencies={"unionOfLayers.SBRDNTD_DBT"})
	def SBRDNTD_DBT(self) -> str:
		''' return string from SBRDNTD_DBT enumeration '''
		return self.unionOfLayers.SBRDNTD_DBT()

	@lineage(dependencies={"unionOfLayers.INTRST_RT_CP"})
	def INTRST_RT_CP(self) -> float:
		return self.unionOfLayers.INTRST_RT_CP()

	@lineage(dependencies={"unionOfLayers.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	@lineage(dependencies={"unionOfLayers.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	@lineage(dependencies={"unionOfLayers.PYMNT_FRQNCY"})
	def PYMNT_FRQNCY(self) -> str:
		''' return string from FRQNCY enumeration '''
		return self.unionOfLayers.PYMNT_FRQNCY()

	@lineage(dependencies={"unionOfLayers.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	@lineage(dependencies={"unionOfLayers.TYP_INTRST_RT"})
	def TYP_INTRST_RT(self) -> str:
		''' return string from TYP_INTRST_RT enumeration '''
		return self.unionOfLayers.TYP_INTRST_RT()

	@lineage(dependencies={"unionOfLayers.CRRNCY_DNMNTN"})
	def CRRNCY_DNMNTN(self) -> str:
		''' return string from CRRNCY enumeration '''
		return self.unionOfLayers.CRRNCY_DNMNTN()

	@lineage(dependencies={"unionOfLayers.INTRST_RT_FLR"})
	def INTRST_RT_FLR(self) -> float:
		return self.unionOfLayers.INTRST_RT_FLR()

	@lineage(dependencies={"unionOfLayers.OBSRVD_AGNT_CD"})
	def OBSRVD_AGNT_CD(self) -> str:
		''' return string from STRNG enumeration '''
		return self.unionOfLayers.OBSRVD_AGNT_CD()

	@lineage(dependencies={"unionOfLayers.INTRST_RT_SPRD"})
	def INTRST_RT_SPRD(self) -> float:
		return self.unionOfLayers.INTRST_RT_SPRD()

	@lineage(dependencies={"unionOfLayers.CMMTMNT_INCPTN"})
	def CMMTMNT_INCPTN(self) -> int:
		return self.unionOfLayers.CMMTMNT_INCPTN()

	@lineage(dependencies={"unionOfLayers.DT_LGL_FNL_MTRTY"})
	def DT_LGL_FNL_MTRTY(self) -> datetime:
		return self.unionOfLayers.DT_LGL_FNL_MTRTY()

	@lineage(dependencies={"unionOfLayers.SYNDCTD_CNTRCT_ID"})
	def SYNDCTD_CNTRCT_ID(self) -> str:
		return self.unionOfLayers.SYNDCTD_CNTRCT_ID()

	@lineage(dependencies={"unionOfLayers.DT_END_INTRST_ONLY"})
	def DT_END_INTRST_ONLY(self) -> datetime:
		return self.unionOfLayers.DT_END_INTRST_ONLY()

	@lineage(dependencies={"unionOfLayers.INTRST_RT_RST_FRQNCY"})
	def INTRST_RT_RST_FRQNCY(self) -> str:
		''' return string from FRQNCY enumeration '''
		return self.unionOfLayers.INTRST_RT_RST_FRQNCY()

	@lineage(dependencies={"unionOfLayers.FV_CHNG_CR_BFR_PRCHS"})
	def FV_CHNG_CR_BFR_PRCHS(self) -> int:
		return self.unionOfLayers.FV_CHNG_CR_BFR_PRCHS()



class ANCRDT_INSTRMNT_C_1_Table :
	ANCRDT_INSTRMNT_C_1_UnionTable = None # unionOfLayersTable
	ANCRDT_INSTRMNT_C_1s = [] #ANCRDT_INSTRMNT_C_1[]
	def  calc_ANCRDT_INSTRMNT_C_1s(self) -> list[ANCRDT_INSTRMNT_C_1] :
		items = [] # ANCRDT_INSTRMNT_C_1[]
		for item in self.ANCRDT_INSTRMNT_C_1_UnionTable.ANCRDT_INSTRMNT_C_1_UnionItems:
			newItem = ANCRDT_INSTRMNT_C_1()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.ANCRDT_INSTRMNT_C_1s = []
		self.ANCRDT_INSTRMNT_C_1s.extend(self.calc_ANCRDT_INSTRMNT_C_1s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

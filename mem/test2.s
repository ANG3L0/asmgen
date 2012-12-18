/*
*	Test generated by:
*	Angelo Wong
*	Yao Hao
*	Lanyue Wang
*	of EECS 578 Fall 2012
*/
#define SCONTEXT PCONTEXT

#define	MAIN_PAGE_NUCLEUS_ALSO
#define	MAIN_PAGE_HV_ALSO
!#define	N_CPUS	64
#define	ENABLE_T0_Fp_exception_ieee_754_0x21
#define	ENABLE_T0_Fp_exception_other_0x22
#define	ENABLE_T0_Fp_disabled_0x20
#define	ENABLE_T0_Illegal_instruction_0x10
#define	ENABLE_T1_Illegal_instruction_0x10
#define	ENABLE_HT0_Illegal_instruction_0x10
#define	ENABLE_HT1_Illegal_instruction_0x10
#define	ENABLE_T0_Clean_Window_0x24
!#define	THREAD_COUNT	64
#define	THREAD_STRIDE	1
#define	SKIP_TRAPCHECK
#define USE_MPGEN_TRAPS

#include "boot.s"
#include "hboot.s"
#include "mmu_custom_intr_handlers.s"
#include "peu_defines.h"

! End includes

	.text
	.global main

main:
	th_fork(processor,%l0)

processor_0:
	ta	T_CHANGE_PRIV
	ldx [%g2+0xfff],%g5
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g3
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g6
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g5
	ldx [%g2+0xfff],%g3
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g3
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g0
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g2
	ldx [%g2+0xfff],%g2
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g2
	ldx [%g2+0xfff],%g3
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g3
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g1
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g1
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g4
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g0
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g2
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g3
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g0
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g7
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g3
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g2
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g2
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g2
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g6
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g6
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g3
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g6
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g3
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g6
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g1
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g0
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g0
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g4
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g3
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g5
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g3
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g6
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g5
	ldx [%g2+0xfff],%g5
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g5
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g2
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g2
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g7
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g0
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g0
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g3
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g6
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g6
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g3
	ldx [%g2+0xfff],%g3
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g3
	ldx [%g2+0xfff],%g4
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g7
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g5
	ldx [%g2+0xfff],%g1
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g2
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g5
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g0
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g0
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g6
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g2
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g6
	ldx [%g2+0xfff],%g6
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g6
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g1
	ldx [%g1+0x160],%g1
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g4
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g0
	ldx [%g1+0x160],%g2
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g1
	ldx [%g2+0xfff],%g5
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g6
	ldx [%g1+0x160],%g7
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g1
	membar #Sync
	membar #Sync
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g7
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g5
	ldx [%g1+0x160],%g3
	stx %g1,[%g1+0x80]
	ldx [%g1+0x160],%g2
	ldx [%g1+0x160],%g7
	ldx [%g1+0x160],%g4
	ldx [%g2+0xfff],%g0
	ldx [%g1+0x160],%g4
	ldx [%g1+0x160],%g3
	ldx [%g1+0x160],%g5
	add %g1,0x0,%l0
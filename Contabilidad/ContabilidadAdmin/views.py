from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pasado(request):
        if request.method == 'POST':
        # -----------------------------------
            Empresa = request.POST['Empresa']
            # Tabla 1
            MPA_S1 = float(request.POST['MPA_S1'])
            MPA_S2 = float(request.POST['MPA_S2'])
            MPA_CS1 = float(request.POST['MPA_CS1'])
            MPA_CS2 = float(request.POST['MPA_CS2'])
        # -----------------------------------
            MPB_S1 = float(request.POST['MPB_S1'])
            MPB_S2 = float(request.POST['MPB_S2'])
            MPB_CS1 = float(request.POST['MPB_CS1'])
            MPB_CS2 = float(request.POST['MPB_CS2'])
        # -----------------------------------
            MPC_S1 = float(request.POST['MPC_S1'])
            MPC_S2 = float(request.POST['MPC_S2'])
            MPC_CS1 = float(request.POST['MPC_CS1'])
            MPC_CS2 = float(request.POST['MPC_CS2'])
        # -----------------------------------
            PA_S1 = float(request.POST['PA_S1'])
            PA_S2 = float(request.POST['PA_S2'])
        # -----------------------------------
            PB_S1 = float(request.POST['PB_S1'])
            PB_S2 = float(request.POST['PB_S2'])
        # -----------------------------------
            PC_S1 = float(request.POST['PC_S1'])
            PC_S2 = float(request.POST['PC_S2'])
        # -----------------------------------
            # Tabla 2
            PV_AS1 = float(request.POST['PV_AS1'])
            PV_BS1 = float(request.POST['PV_BS1'])
            PV_CS1 = float(request.POST['PV_CS1'])
        # -----------------------------------
            PV_AS2 = float(request.POST['PV_AS2'])
            PV_BS2 = float(request.POST['PV_BS2'])
            PV_CS2 = float(request.POST['PV_CS2'])
        # -----------------------------------
            VP_AS1 = float(request.POST['VP_AS1'])
            VP_BS1 = float(request.POST['VP_BS1'])
            VP_CS1 = float(request.POST['VP_CS1'])
        # float(-----------------------------------
            VP_AS2 = float(request.POST['VP_AS2'])
            VP_BS2 = float(request.POST['VP_BS2'])
            VP_CS2 = float(request.POST['VP_CS2'])
        # -----------------------------------
            # Tabla float(3
            GAV_D = float(request.POST['GAV_D'])
            GAV_SYS = float(request.POST['GAV_SYS'])
            GAV_Com = float(request.POST['GAV_Com'])
            GAV_VS1 = float(request.POST['GAV_VS1'])
            GAV_VS2 = float(request.POST['GAV_VS2'])
            GAV_IPP = float(request.POST['GAV_IPP'])
        # -----------------------------------
            # Tabla float(4
            GIF_D = float(request.POST['GIF_D'])
            GIF_Seg = float(request.POST['GIF_Seg'])
            GIF_MS1 = float(request.POST['GIF_MS1'])
            GIF_MS2 = float(request.POST['GIF_MS2'])
            GIF_ES1 = float(request.POST['GIF_ES1'])
            GIF_ES2 = float(request.POST['GIF_ES2'])
            GIF_VA = float(request.POST['GIF_VA'])
        # ----------------------------------
            # Tabla float(5
            Eq_Nv = float(request.POST['Eq_Nv'])
            SC_AAn = float(request.POST['SC_AAn'])
            VP_AAc = float(request.POST['VP_AAc'])
            SP_AAn = float(request.POST['SP_AAn'])
            CP_AAc = float(request.POST['CP_AAc'])
        # -----------------------------------
            # Tabla 6
            Year = int(request.POST['Year'])
            Efectivo = float(request.POST['Efectivo'])
            Proveedores = float(request.POST['Proveedores'])
            Clientes = float(request.POST['Clientes'])
            DocPP = float(request.POST['DocPP'])
            DD = float(request.POST['DD'])
            ISRxP = float(request.POST['ISRxP'])
            FunEmp = float(request.POST['FunEmp'])
            TPCP = float(request.POST.get('TPCP',False)) 
            InvMat = float(request.POST['InvMat']) 
            InvPT = float(request.POST['InvPT']) 
            PrBc = float(request.POST['PrBc']) 
            TAC = float(request.POST.get('TAC', False)) 
            TPLP = float(request.POST.get('TPLP', False)) 
            Terreno = float(request.POST['Terreno']) 
            Pasiv = float(request.POST.get('Pasiv',False)) 
            PyE = float(request.POST['PyE']) 
            DepA = float(request.POST['DepA']) 
            TANC = float(request.POST.get('TANC', False)) 
            CapCon = float(request.POST['CapCon']) 
            CapGan = float(request.POST['CapGan']) 
            CCTotal = float(request.POST.get('CCTotal',False)) 
            ActTot = float(request.POST.get('ActTot',False)) 
            SPyC = float(request.POST.get('SPyC',False)) 
        # -----------------------------------
            # Tabla 7
            RM_MPA_PA = float(request.POST['RM_MPA_PA'])
            RM_MPA_PB = float(request.POST['RM_MPA_PB'])
            RM_MPA_PC = float(request.POST['RM_MPA_PC'])
        # -----------------------------------
            RM_MPB_PA = float(request.POST['RM_MPB_PA'])
            RM_MPB_PB = float(request.POST['RM_MPB_PB'])
            RM_MPB_PC = float(request.POST['RM_MPB_PC'])
        # -----------------------------------
            RM_MPC_PA = float(request.POST['RM_MPC_PA'])
            RM_MPC_PB = float(request.POST['RM_MPC_PB'])
            RM_MPC_PC = float(request.POST['RM_MPC_PC'])
        # -----------------------------------
            RM_MO_PA = float(request.POST['RM_MO_PA'])
            RM_MO_PB = float(request.POST['RM_MO_PB'])
            RM_MO_PC = float(request.POST['RM_MO_PC'])
        # -----------------------------------
            # Tabla 8
            MOD_S1 = float(request.POST['MOD_S1'])
            MOD_S2 = float(request.POST['MOD_S2'])
        # -----------------------------------

        # Multiplicaciones:
            # I PRESUPUESTO DE OPERACIÓN
            # 1. Presupuesto de ventas:
            PA_IV_S1 = VP_AS1 * PV_AS1
            PA_IV_S2 = VP_AS2 * PV_AS2
            Total_PAI = PA_IV_S1 + PA_IV_S2
            #--
            PB_IV_S1 = VP_BS1 * PV_BS1
            PB_IV_S2 = VP_BS2 * PV_BS2
            Total_PBI = PB_IV_S1 + PB_IV_S2
            #--
            PC_IV_S1 = VP_CS1 * PV_CS1
            PC_IV_S2 = VP_CS2 * PV_CS2
            Total_PCI = PC_IV_S1 + PC_IV_S2
            #--
            PVABC_S1 = PA_IV_S1 + PB_IV_S1 + PC_IV_S1
            PVABC_S2 = PA_IV_S2 + PB_IV_S2 + PC_IV_S2
            Total_PV = PVABC_S1 + PVABC_S2

            # 2. Determinación del Saldo de Clientes y Flujo de Entradas
            Total_Clientes_2001 = Total_PV + Clientes
            Por_Cobranza2000 = (SC_AAn/100) * Clientes
            Por_Cobranza2001 = (VP_AAc/100) * Total_PV
            TotalEntradas2001 = Por_Cobranza2000 + Por_Cobranza2001
            Saldo_Clientes2001 = Total_Clientes_2001 - TotalEntradas2001

            # 3. Presupuesto de Producción
            YearNow = Year + 1
            B45 = VP_AS1 + PA_S1
            B46 = B45 - PA_S1
            B47 = B45 - B46
            C45 = VP_AS2 + PA_S2
            C46 = C45 - PA_S1
            C47 = C45 - C46
            D43 = VP_AS1 + VP_AS2
            D45 = D43 + PA_S2
            D47 = B47
            otro = B46 + C46
            D50 = VP_BS1 + VP_BS2
            B52 = VP_BS1 + PB_S1
            C52 = VP_BS2 + PB_S2
            D52 = D50 + PB_S2
            B54 = B52 - PB_S1
            C54 = C52 - PB_S1
            D54 = D52 - PB_S1
            D57 = VP_CS1 + VP_CS2
            B59 = VP_CS1 + PC_S1
            C59 = VP_CS2 + PC_S2
            D59 = D57 + PC_S2
            B61 = B59 - PC_S1
            C61 = C59 - PC_S1
            D61 = D59 - PC_S1

            # 6 Determinacion
            TotalProveedoresNow = Proveedores * (SP_AAn/100)

            # 8 Presupuesto de Gastos
            GIF_DM = GIF_D/2
            GIF_SegM = GIF_Seg/2
            GIF_MTotal = GIF_MS1 + GIF_MS2
            GIF_ETotal = GIF_ES1 + GIF_ES2
            GIF_VAM = GIF_VA/2
            TotalGIF1 = GIF_DM + GIF_SegM + GIF_MS1 + GIF_ES1 + GIF_VAM
            TotalGIF2 = GIF_DM + GIF_SegM + GIF_MS2 + GIF_ES2 + GIF_VAM
            TotalGIF = TotalGIF1 + TotalGIF2


            # 9 Presupuesto de Gastos de Operación
            GAV_DM = GAV_D/2
            GAV_SYSM = GAV_SYS/2
            GAV_Com1 = (GAV_Com/100)*PVABC_S1
            GAV_Com2 = (GAV_Com/100)*PVABC_S2
            GAV_ComTotal = GAV_Com2 + GAV_Com1
            GAV_VTotal = GAV_VS1 + GAV_VS2
            GAV_IPPM = GAV_IPP/2
            GOTotal1 = GAV_DM + GAV_SYSM + GAV_Com1 + GAV_VS1 + GAV_IPPM
            GOTotal2 = GAV_DM + GAV_SYSM + GAV_Com2 + GAV_VS2 + GAV_IPPM
            GOTotal = GOTotal1 + GOTotal2

            # 10 Determinacion del Costo Unitario de Produccion
            DCUAA = MPA_CS2 * RM_MPA_PA
            DCUAB = MPB_CS2 * RM_MPB_PA
            DCUAC = MPC_CS2 * RM_MPC_PA
            DCUAMO = MOD_S2 * RM_MO_PA

            DCUBA = MPA_CS2 * RM_MPA_PB
            DCUBB = MPB_CS2 * RM_MPB_PB
            DCUBC = MPC_CS2 * RM_MPC_PB
            DCUBMO = MOD_S2 * RM_MO_PB

            DCUCA = MPA_CS2 * RM_MPA_PC
            DCUCB = MPB_CS2 * RM_MPB_PC
            DCUCC = MPC_CS2 * RM_MPC_PC
            DCUCMO = MOD_S2 * RM_MO_PC

            # 11 Valuación de Inventarios FInales
            IFMMA = MPA_S2 * MPA_CS2
            IFMMB = MPB_S2 * MPB_CS2
            IFMMC = MPC_S2 * MPC_CS2
            IFM = IFMMA + IFMMB + IFMMC

            # Estado de Flujo de Efectivo
            TotalEntry = VP_AAc + SC_AAn
            EfectivoDisponible = TotalEntry + Efectivo

        return render(request,'TablasEvidencia.html',{
            'Empresa' : Empresa,
            'otro' : otro,
            'MPA_S1' : MPA_S1,
            'MPA_S2' : MPA_S2,
            'MPA_CS1' : MPA_CS1,
            'MPA_CS2' : MPA_CS2,
            'MPB_S1' : MPB_S1,
            'MPB_S2' : MPB_S2, 
            'MPB_CS1' : MPB_CS1, 
            'MPB_CS2' : MPB_CS2,  
            'MPC_S1' : MPC_S1,  
            'MPC_S2' : MPC_S2,  
            'MPC_CS1' : MPC_CS1,  
            'MPC_CS2' : MPC_CS2,  
            'PA_S1' : PA_S1,  
            'PA_S2' : PA_S2,  
            'PB_S1' : PB_S1,  
            'PB_S2' : PB_S2,  
            'PC_S1' : PC_S1,  
            'PC_S2' : PC_S2,  
            'PV_AS1' : PV_AS1,  
            'PV_BS1' : PV_BS1,  
            'PV_CS1' : PV_CS1,  
            'PV_AS2' : PV_AS2,  
            'PV_BS2' : PV_BS2,  
            'PV_CS2' : PV_CS2,  
            'VP_AS1' : VP_AS1,  
            'VP_BS1' : VP_BS1,  
            'VP_CS1' : VP_CS1,  
            'VP_AS2' : VP_AS2,  
            'VP_BS2' : VP_BS2,  
            'VP_CS2' : VP_CS2,  
            'GAV_D' : GAV_D,  
            'GAV_SYS' : GAV_SYS,  
            'GAV_Com' : GAV_Com,  
            'GAV_VS1' : GAV_VS1,  
            'GAV_VS2' : GAV_VS2,  
            'GAV_IPP' : GAV_IPP,  
            'GIF_D' : GIF_D,
            'GIF_DM' : GIF_DM,  
            'GIF_Seg' : GIF_Seg,  
            'GIF_MS1' : GIF_MS1,  
            'GIF_MS2' : GIF_MS2,  
            'GIF_ES1' : GIF_ES1,  
            'GIF_ES2' : GIF_ES2,  
            'GIF_VA' : GIF_VA,  
            'Eq_Nv' : Eq_Nv,  
            'SC_AAn' : SC_AAn,  
            'VP_AAc' : VP_AAc,  
            'SP_AAn' : SP_AAn,  
            'CP_AAc' : CP_AAc,  
            'Year' : Year,  
            'Efectivo' : Efectivo,  
            'Proveedores' : Proveedores,  
            'Clientes' : Clientes,  
            'DocPP' : DocPP,  
            'DD' : DD,  
            'ISRxP' : ISRxP,  
            'FunEmp' : FunEmp,  
            'TPCP' : TPCP,   
            'InvMat' : InvMat,   
            'InvPT' : InvPT,   
            'PrBc' : PrBc,   
            'TAC' : TAC,   
            'TPLP' : TPLP,   
            'Terreno' : Terreno,   
            'Pasiv' : Pasiv,   
            'PyE' : PyE,   
            'DepA' : DepA,   
            'TANC' : TANC,   
            'CapCon' : CapCon,   
            'CapGan' : CapGan,   
            'CCTotal' : CCTotal,   
            'ActTot' : ActTot,   
            'SPyC' : SPyC,   
            'RM_MPA_PA' : RM_MPA_PA,  
            'RM_MPA_PB' : RM_MPA_PB,  
            'RM_MPA_PC' : RM_MPA_PC,  
            'RM_MPB_PA' : RM_MPB_PA,  
            'RM_MPB_PB' : RM_MPB_PB,  
            'RM_MPB_PC' : RM_MPB_PC,  
            'RM_MPC_PA' : RM_MPC_PA,  
            'RM_MPC_PB' : RM_MPC_PB,  
            'RM_MPC_PC' : RM_MPC_PC,  
            'RM_MO_PA' : RM_MO_PA,  
            'RM_MO_PB' : RM_MO_PB,  
            'RM_MO_PC' : RM_MO_PC,  
            'MOD_S1' : MOD_S1,  
            'MOD_S2' : MOD_S2,
            'MPA_S2' : MPA_S2,
            'MPA_CS1' : MPA_CS1,
            'MPA_CS2' : MPA_CS2,
            'MPB_S1' : MPB_S1,
            'MPB_S2' : MPB_S2, 
            'MPB_CS1' : MPB_CS1, 
            'PA_IV_S1' : PA_IV_S1,
            'PA_IV_S2' : PA_IV_S2,
            'Total_PAI' : Total_PAI,
            'PB_IV_S1' : PB_IV_S1,
            'PB_IV_S2' : PB_IV_S2,
            'Total_PBI' : Total_PBI,
            'PC_IV_S1' : PC_IV_S1,
            'PC_IV_S2' : PC_IV_S2,
            'Total_PCI' : Total_PCI,
            'PVABC_S1' : PVABC_S1,
            'PVABC_S2' : PVABC_S2,
            'Total_PV' : Total_PV,
            'Total_Clientes_2001' : Total_Clientes_2001,
            'Por_Cobranza2000' : Por_Cobranza2000,
            'Por_Cobranza2001' : Por_Cobranza2001,
            'TotalEntradas2001' : TotalEntradas2001,
            'Saldo_Clientes2001' : Saldo_Clientes2001,
            'B45' : B45,
            'B46' : B46,
            'B47' : B47,
            'C45' : C45,
            'C46' : C46,
            'C47' : C47,
            'D43' : D43,
            'D45' : D45,
            'D47' : D47,
            'D50' : D50,
            'B52' : B52,
            'C52' : C52,
            'D52' : D52,
            'B54' : B54,
            'C54' : C54,
            'D54' : D54,
            'D57' : D57,
            'B59' : B59,
            'C59' : C59,
            'D59' : D59,
            'B61' : B61,
            'C61' : C61,
            'D61' : D61,
            'YearNow' : YearNow,
            'GAV_DM' : GAV_DM,
            'GIF_SegM' : GIF_SegM,
            'GIF_MTotal' : GIF_MTotal,
            'GIF_ETotal' : GIF_ETotal,
            'GIF_VAM' : GIF_VAM,
            'TotalGIF1' : TotalGIF1,
            'TotalGIF2' : TotalGIF2,
            'TotalGIF' : TotalGIF,
            'GAV_DM' : GAV_DM,
            'GAV_SYSM' : GAV_SYSM,
            'GAV_Com1' : GAV_Com1,
            'GAV_Com2' : GAV_Com2,
            'GAV_ComTotal' : GAV_ComTotal,
            'GAV_VTotal' : GAV_VTotal,
            'GAV_IPPM' : GAV_IPPM,
            'GOTotal1' : GOTotal1,
            'GOTotal2' : GOTotal2,
            'GOTotal' : GOTotal,
            'DCUAA' : DCUAA,
            'DCUAB' : DCUAB,
            'DCUAC' : DCUAC,
            'DCUAMO' : DCUAMO,
            'DCUBA' : DCUBA,
            'DCUBB' : DCUBB,
            'DCUBC' : DCUBC,
            'DCUBMO' : DCUBMO,
            'DCUCA' : DCUCA,
            'DCUCB' : DCUCB,
            'DCUCC' : DCUCC,
            'DCUCMO' : DCUCMO,
            'IFMMA' : IFMMA,
            'IFMMB' : IFMMB,
            'IFMMC' : IFMMC,
            'IFM' : IFM,
            'TotalEntry' : TotalEntry,
            'EfectivoDisponible' : EfectivoDisponible,
            'TotalProveedoresNow' : TotalProveedoresNow
        })

def resultado(request):
    return render(request, 'TablasEvidencia.html')
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pasado(request):
    try:
        if request.method == 'POST':
        # -----------------------------------
            # Tabla 1
            MPA_S1 = request.POST['MPA_S1']
            MPA_S2 = request.POST['MPA_S2']
            MPA_CS1 = request.POST['MPA_CS1']
            MPA_CS2 = request.POST['MPA_CS2']
        # -----------------------------------
            MPB_S1 = request.POST['MPB_S1']
            MPB_S2 = request.POST['MPB_S2']
            MPB_CS1 = request.POST['MPB_CS1']
            MPB_CS2 = request.POST['MPB_CS2']
        # -----------------------------------
            MPC_S1 = request.POST['MPC_S1']
            MPC_S2 = request.POST['MPC_S2']
            MPC_CS1 = request.POST['MPC_CS1']
            MPC_CS2 = request.POST['MPC_CS2']
        # -----------------------------------
            PA_S1 = request.POST['PA_S1']
            PA_S2 = request.POST['PA_S2']
        # -----------------------------------
            PA_S1 = request.POST['PB_S1']
            PA_S2 = request.POST['PB_S2']
        # -----------------------------------
            PA_S1 = request.POST['PC_S1']
            PA_S2 = request.POST['PC_S2']
        # -----------------------------------
            # Tabla 2
            PV_AS1 = request.POST['PV_AS1']
            PV_BS1 = request.POST['PV_BS1']
            PV_CS1 = request.POST['PV_CS1']
        # -----------------------------------
            PV_AS2 = request.POST['PV_AS2']
            PV_BS2 = request.POST['PV_BS2']
            PV_CS2 = request.POST['PV_CS2']
        # -----------------------------------
            VP_AS1 = request.POST['VP_AS1']
            VP_BS1 = request.POST['VP_BS1']
            VP_CS1 = request.POST['VP_CS1']
        # -----------------------------------
            VP_AS2 = request.POST['VP_AS2']
            VP_BS2 = request.POST['VP_BS2']
            VP_CS2 = request.POST['VP_CS2']
        # -----------------------------------
            # Tabla 3
            GAV_D = request.POST['GAV_D']
            GAV_SYS = request.POST['GAV_SYS']
            GAV_Com = request.POST['GAV_Com']
            GAV_VS1 = request.POST['GAV_VS1']
            GAV_VS2 = request.POST['GAV_VS2']
            GAV_IPP = request.POST['GAV_IPP']
        # -----------------------------------
            # Tabla 4
            GIF_D = request.POST['GIF_D']
            GIF_Seg = request.POST['GIF_Seg']
            GIF_MS1 = request.POST['GIF_MS1']
            GIF_MS2 = request.POST['GIF_MS2']
            GIF_ES1 = request.POST['GIF_ES1']
            GIF_ES2 = request.POST['GIF_ES2']
            GIF_VA = request.POST['GIF_VA']
        # -----------------------------------
            # Tabla 5
            Eq_Nv = request.POST['Eq_Nv']
            SC_AAn = request.POST['SC_AAn']
            VP_AAc = request.POST['VP_AAc']
            SP_AAn = request.POST['SP_AAn']
            CP_AAc = request.POST['CP_AAc']
        # -----------------------------------
            # Tabla 6
            Year = request.post['Year']
            Efectivo = request.post['Efectivo']
            Proveedores = request.post['Proveedores']
            Clientes = request.post['Clientes']
            DocPP = request.post['DocPP']
            DD = request.post['DD']
            ISRxP = request.post['ISRxP']
            FunEmp = request.post['FunEmp']
            TPCP = request.post['TPCP'] 
            InvMat = request.post['InvMat'] 
            InvPT = request.post['InvPT'] 
            PrBc = request.post['PrBc'] 
            TAC = request.post['TAC'] 
            TPLP = request.post['TPLP'] 
            Terreno = request.post['Terreno'] 
            Pasiv = request.post['Pasiv'] 
            PyE = request.post['PyE'] 
            DepA = request.post['DepA'] 
            TANC = request.post['TANC'] 
            CapCon = request.post['CapCon'] 
            CapGan = request.post['CapGan'] 
            CCTotal = request.post['CCTotal'] 
            ActTot = request.post['ActTot'] 
            SPyC = request.post['SPyC'] 
        # -----------------------------------
            # Tabla 7
            RM_MPA_PA = request.POST['RM_MPA_PA']
            RM_MPA_PB = request.POST['RM_MPA_PB']
            RM_MPA_PC = request.POST['RM_MPA_PC']
        # -----------------------------------
            RM_MPB_PA = request.POST['RM_MPB_PA']
            RM_MPB_PB = request.POST['RM_MPB_PB']
            RM_MPB_PC = request.POST['RM_MPB_PC']
        # -----------------------------------
            RM_MPC_PA = request.POST['RM_MPC_PA']
            RM_MPC_PB = request.POST['RM_MPC_PB']
            RM_MPC_PC = request.POST['RM_MPC_PC']
        # -----------------------------------
            RM_MO_PA = request.POST['RM_MO_PA']
            RM_MO_PB = request.POST['RM_MO_PB']
            RM_MO_PC = request.POST['RM_MO_PC']
        # -----------------------------------
            # Tabla 8
            MOD_S1 = request.POST['MOD_S1']
            MOD_S2 = request.POST['MOD_S2']
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
            Total_PCI = PC_IV_S1 * PC_IV_S2
            #--
            PVABC_S1 = PA_IV_S1 + PB_IV_S1 + PC_IV_S1
            PVABC_S2 = PA_IV_S2 + PB_IV_S2 + PC_IV_S2
            Total_PV = PVABC_S1 + PVABC_S2

            # 2. Determinación del Saldo de Clientes y Flujo de Entradas
            Total_Clientes_2001 = Total_PV + Clientes
            Por_Cobranza2000 = float(f'0.{SC_AAn}') * Clientes
            Por_Cobranza2001 = float(f'0.{VP_AAc}') * Total_PV
            TotalEntradas2001 = Por_Cobranza2000 + Por_Cobranza2001
            Saldo_Clientes2001 = Total_Clientes_2001 - TotalEntradas2001

            # 3. Presupuesto de Producción
            PP_A_TU_S1 = 0


        return HttpResponse('Proceso correcto')
    except:
        return HttpResponse('Error')

def resultado(request):
    return render(request, 'TablasEvidencia.html')
# Gypsy Bot - Anpassningar för 15-minuters Timeframe

## Översikt
Anpassning från 1H till 15min = 4x snabbare
- Längder divideras med ~4
- Procentsatser (TP/SL) divideras med ~3-4

---

## 📊 GUPPY MMA LÄNGDER (rad 157-179)
```pinescript
// FÖRE (1H):
ma1SPI = 3, ma2SPI = 6, ma3SPI = 9, ma4SPI = 12, ma5SPI = 15, ma6SPI = 18, ma7SPI = 21
ma8SPI = 24, ma9SPI = 27, ma10SPI = 30, ma11SPI = 33, ma12SPI = 36
ma13SPI = 39, ma14SPI = 42, ma15SPI = 45, ma16SPI = 48, ma17SPI = 51, ma18SPI = 54
ma19SPI = 57, ma20SPI = 60, ma21SPI = 63, ma22SPI = 66
ma23SPI = 200

// EFTER (15MIN):
ma1SPI = 1, ma2SPI = 2, ma3SPI = 2, ma4SPI = 3, ma5SPI = 4, ma6SPI = 5, ma7SPI = 5
ma8SPI = 6, ma9SPI = 7, ma10SPI = 8, ma11SPI = 8, ma12SPI = 9
ma13SPI = 10, ma14SPI = 11, ma15SPI = 11, ma16SPI = 12, ma17SPI = 13, ma18SPI = 14
ma19SPI = 14, ma20SPI = 15, ma21SPI = 16, ma22SPI = 17
ma23SPI = 50
```

## 📈 TSI PARAMETRAR (rad 230-243)
```pinescript
// FÖRE:
longTSI = 25
shortTSI = 13
signalTSI = 50
sig1smoother = ta.ema(sig1SPI, 14)
sig2smoother = ta.ema(sig2SPI, 5)
SSGuppy = ta.ema(sig1smoother, 4000)

// EFTER:
longTSI = 6
shortTSI = 3
signalTSI = 12
sig1smoother = ta.ema(sig1SPI, 4)
sig2smoother = ta.ema(sig2SPI, 1)
SSGuppy = ta.ema(sig1smoother, 1000)
```

## 🎯 HSRS PARAMETRAR (rad 249, 272)
```pinescript
// FÖRE:
lengthHSRS = 1000
nm_HSRS = 21

// EFTER:
lengthHSRS = 250
nm_HSRS = 5
```

## 📊 RSI MODULER
### Smoothed RSI (Sök efter "Slength")
```pinescript
// FÖRE:
Slength = input(7, 'Fast RSI Length', group = RSIMOD)
SlengthSlow = input(35, 'Slow RSI Length', group = RSIMOD)

// EFTER:
Slength = input(2, 'Fast RSI Length', group = RSIMOD)
SlengthSlow = input(9, 'Slow RSI Length', group = RSIMOD)
```

### QQE RSI (Sök efter "lengthQQE")
```pinescript
// FÖRE:
lengthQQE = input.int(14, 'QQE Module - RSI Length', minval = 1, group = RSIMOD)

// EFTER:
lengthQQE = input.int(4, 'QQE Module - RSI Length', minval = 1, group = RSIMOD)
```

## 🔧 MODULE PARAMETRAR

### First Module - Modified Slope Angle (rad 422)
```pinescript
// FÖRE:
MASLength = input.int(14, 'Modified Slope Angle - Length (Default=14)', minval = 0, group = TEMod1)

// EFTER:
MASLength = input.int(4, 'Modified Slope Angle - Length (Default=4)', minval = 0, group = TEMod1)
```

### Second Module - CTI (Sök efter "LengthCTI")
```pinescript
// FÖRE:
LengthCTI = 14

// EFTER:
LengthCTI = 4
```

### Third Module - Ehlers Roofing Filter (Sök efter "highpassLengthERF")
```pinescript
// FÖRE:
highpassLengthERF = 48
ssfLengthERF = 17

// EFTER:
highpassLengthERF = 12
ssfLengthERF = 4
```

### Fourth Module - Forecast Oscillator (Sök efter "lengthFO")
```pinescript
// FÖRE:
lengthFO = 14

// EFTER:
lengthFO = 4
```

### Fifth Module - Chandelier ATR (Sök efter "Lengthz")
```pinescript
// FÖRE:
Lengthz = 22
ATRPeriod = 22
Mult = input(title = 'ATR Multiplier', defval = 3, group = TEMod5)
windowBBQ = input(title = 'Bull Bear Qualifier - Lookback Window:', defval = 7, group = TEMod5)

// EFTER:
Lengthz = 6
ATRPeriod = 6
Mult = input(title = 'ATR Multiplier', defval = 3, group = TEMod5)  // Behåll 3
windowBBQ = input(title = 'Bull Bear Qualifier - Lookback Window:', defval = 2, group = TEMod5)
```

### Sixth Module - CMB (Sök efter "CMBmovingAverageLength")
```pinescript
// FÖRE:
CMBmovingAverageLength1 = 20
CMBmovingAverageLength2 = 50
CMB_SmootherLength = 7

// EFTER:
CMBmovingAverageLength1 = 5
CMBmovingAverageLength2 = 12
CMB_SmootherLength = 2
```

### Seventh Module - DIC (Sök efter "fast_lengthDIC")
```pinescript
// FÖRE:
int fast_lengthDIC = 10
int slow_lengthDICPRE = 2000

// EFTER:
int fast_lengthDIC = 3
int slow_lengthDICPRE = 500
```

### Eighth Module - MTI (Sök efter "malen1")
```pinescript
// FÖRE:
malen1 = input.int(defval = 14, title = 'MTI Agressive Length', minval = 1, group = TEMod8)
malen2 = input.int(defval = 35, title = 'MTI Normal Length', minval = 1, group = TEMod8)

// EFTER:
malen1 = input.int(defval = 4, title = 'MTI Agressive Length', minval = 1, group = TEMod8)
malen2 = input.int(defval = 9, title = 'MTI Normal Length', minval = 1, group = TEMod8)
```

### Ninth Module - Ichimoku (Sök efter "conversionPeriodsICHICLOUD")
```pinescript
// FÖRE:
conversionPeriodsICHICLOUD = 9
basePeriodsICHICLOUD = 26
laggingSpan2PeriodsICHICLOUD = 52
displacementICHICLOUD = 26

// EFTER:
conversionPeriodsICHICLOUD = 2
basePeriodsICHICLOUD = 7
laggingSpan2PeriodsICHICLOUD = 13
displacementICHICLOUD = 7
```

### Tenth Module - Harmonic (Sök efter "lenHO")
```pinescript
// FÖRE:
lenHO = 14

// EFTER:
lenHO = 4
```

### Eleventh Module - HSRS Compression (Sök efter "lengthComp")
```pinescript
// FÖRE:
lengthComp = input.int(21, title = 'HSRS Compression Length', minval = 1, group = TEMod11)

// EFTER:
lengthComp = input.int(5, title = 'HSRS Compression Length', minval = 1, group = TEMod11)
```

### Eleventh Module - Super AO (Sök efter "AOfastLength")
```pinescript
// FÖRE:
AOfastLength = input(title = 'AO Fast Length', defval = 14)
AOslowLength = input(title = 'AO Slow Length', defval = 500)
AOSmoothInput = input(title = 'AO Smoother length', defval = 21)
STPeriods = input(title = 'ST ATR Period', defval = 14)

// EFTER:
AOfastLength = input(title = 'AO Fast Length', defval = 4)
AOslowLength = input(title = 'AO Slow Length', defval = 125)
AOSmoothInput = input(title = 'AO Smoother length', defval = 5)
STPeriods = input(title = 'ST ATR Period', defval = 4)
```

### Twelfth Module - Fisher Transform (Sök efter "lengthFTMTF")
```pinescript
// FÖRE:
lengthFTMTF = 10

// EFTER:
lengthFTMTF = 3
```

## 🛡️ ADX PARAMETRAR (Sök efter "ADXlen")
```pinescript
// FÖRE:
ADXlen = input.int(25, minval = 1, title = 'ADX DI Length', group = TEADX)
ADXlensig = 14
ADXlenDPT = 4
ADXThreshold = input(10, title = 'Primary Order Activation Threshold (Default = 10)', group = TEADX)
ADXSepThreshold = input(8, title = 'Secondary Order Activation Threshold (Default = 8)', group = TEADX)

// EFTER:
ADXlen = input.int(6, minval = 1, title = 'ADX DI Length', group = TEADX)
ADXlensig = 4
ADXlenDPT = 1
ADXThreshold = input(8, title = 'Primary Order Activation Threshold (Default = 8)', group = TEADX)
ADXSepThreshold = input(6, title = 'Secondary Order Activation Threshold (Default = 6)', group = TEADX)
```

## 💰 RISK MANAGEMENT - TP/SL (VIKTIGT!)

### Trailing Stop (Sök efter "tsActivationPre")
```pinescript
// FÖRE:
tsActivationPre = input.float(18.0, 'Trailing Stop Activation (%)', minval = 0, step = 0.1, group = TSMod) / 100
tsPre = input.float(6.0, 'Trailing Stop (%)', minval = 0, step = 0.1, group = TSMod) / 100

// EFTER:
tsActivationPre = input.float(4.5, 'Trailing Stop Activation (%)', minval = 0, step = 0.1, group = TSMod) / 100
tsPre = input.float(1.5, 'Trailing Stop (%)', minval = 0, step = 0.1, group = TSMod) / 100
```

### Take Profit (Sök efter "isTP")
```pinescript
// FÖRE:
tp = input.float(12.0, 'Take Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100
ttp = input.float(2.5, 'Trailing Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100

// EFTER:
tp = input.float(3.0, 'Take Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100
ttp = input.float(0.6, 'Trailing Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100
```

### Staged Take Profits (Sök efter "Stp1Per")
```pinescript
// FÖRE:
Stp1Per = input.float(10.0, '1st Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)
Stp1Trail = input.float(5.0, '1st Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp2Per = input.float(20.0, '2nd Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)
Stp2Trail = input.float(10.0, '2nd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp3Per = input.float(30.0, '3rd Level - Take Profit Activation Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp3Trail = input.float(5.0, '3rd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)

// EFTER:
Stp1Per = input.float(2.5, '1st Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)
Stp1Trail = input.float(1.2, '1st Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp2Per = input.float(5.0, '2nd Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)
Stp2Trail = input.float(2.5, '2nd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp3Per = input.float(7.5, '3rd Level - Take Profit Activation Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
Stp3Trail = input.float(1.2, '3rd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)
```

### Stop Loss (Sök efter "isSLPre")
```pinescript
// FÖRE:
slPre = input.float(18.0, 'Stop Loss (%)', minval = 0, step = 0.1, group = SLMod) / 100

// EFTER:
slPre = input.float(4.5, 'Stop Loss (%)', minval = 0, step = 0.1, group = SLMod) / 100
```

### DCA (Sök efter "isDCA")
```pinescript
// FÖRE:
DCA = input.float(1.0, 'DCA Threshold(%)', minval = 0, step = 0.1, group = DCAMod) / 100

// EFTER:
DCA = input.float(0.25, 'DCA Threshold(%)', minval = 0, step = 0.1, group = DCAMod) / 100
```

## 🔥 DPT (DUMP PROTECTION TEAM)

### MTI Kicker (Sök efter "KickerPercentUpTrendPre")
```pinescript
// FÖRE:
KickerPercentUpTrendPre = input.float(2.0, 'MTI Kicker Activation (%) - Up Trend', minval = 0, step = 0.1, group = DPTMod)
KickerPercentDnTrend = input.float(6.0, 'MTI Kicker Activation (%) - Down Trend', minval = 0, step = 0.1, group = DPTMod)

// EFTER:
KickerPercentUpTrendPre = input.float(0.5, 'MTI Kicker Activation (%) - Up Trend', minval = 0, step = 0.1, group = DPTMod)
KickerPercentDnTrend = input.float(1.5, 'MTI Kicker Activation (%) - Down Trend', minval = 0, step = 0.1, group = DPTMod)
```

### ESPF (Sök efter "fastLengthESPF")
```pinescript
// FÖRE:
fastLengthESPF = 40
slowLengthESPF = 60

// EFTER:
fastLengthESPF = 10
slowLengthESPF = 15
```

## 📉 BOLLINGER BANDS (Sök efter "lengthMBB")
```pinescript
// FÖRE:
lengthMBB = 34

// EFTER:
lengthMBB = 8
```

### BB MESA Trading (Sök efter "BBtsActivate")
```pinescript
// FÖRE:
BBtsActivate = input.float(2.0, 'MESA ONLY - Trailing Stop Activation (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100
tsbb = input.float(1.0, 'Trailing Stop (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100

// EFTER:
BBtsActivate = input.float(0.5, 'MESA ONLY - Trailing Stop Activation (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100
tsbb = input.float(0.25, 'Trailing Stop (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100
```

## 🎯 ATS (ADAPTIVE TRAILING STOP)

### EMA (Sök efter "lenEMA")
```pinescript
// FÖRE:
lenEMA = 50

// EFTER:
lenEMA = 12
```

### ATS Factor (Sök efter "atsFacInput")
```pinescript
// FÖRE:
atsFacInput = input(100, 'ATS Stop Factor (0+)', group = SLMod2)

// EFTER:
atsFacInput = input(100, 'ATS Stop Factor (0+)', group = SLMod2)  // Behåll 100
```

### RSI Stop (Sök efter "McGinleyRSIS")
```pinescript
// FÖRE (i McGinleyRSIS funktionen):
rsi_maRSIS = McGinleyRSIS(close, 14)
ATRRSIS = ta.atr(27)

// EFTER:
rsi_maRSIS = McGinleyRSIS(close, 4)
ATRRSIS = ta.atr(7)
```

## 🌊 DPT KOMPONENTER

### LagF (Sök efter "alphaLAGF")
```pinescript
// FÖRE:
alphaLAGF = 0.2

// EFTER:
alphaLAGF = 0.2  // Behåll 0.2 (procent-baserad)
```

### KJBB (Sök efter "basePeriodsKJBB")
```pinescript
// FÖRE:
basePeriodsKJBB = 14
displacementKJBB = 14
BB_lengthKJBB = 7

// EFTER:
basePeriodsKJBB = 4
displacementKJBB = 4
BB_lengthKJBB = 2
```

### Super Z (Sök efter "len5SZ")
```pinescript
// FÖRE:
st_periodSZ = 30

// EFTER:
st_periodSZ = 8
```

### Linear Regression (Sök efter "clenLRS")
```pinescript
// FÖRE:
clenLRS = 50
slenLRS = 5
glenLRS = 13

// EFTER:
clenLRS = 12
slenLRS = 1
glenLRS = 3
```

---

## ⚙️ ANDRA VIKTIGA PARAMETRAR

### Pi Cycle (Sök efter "ln_ma_bottomlong")
```pinescript
// FÖRE:
ln_ma_bottomlong = 471
ln_ma_bottomshort = 150

// EFTER:
ln_ma_bottomlong = 118  // 471/4
ln_ma_bottomshort = 38  // 150/4
```

---

## 📝 SAMMANFATTNING

### HUVUDÄNDRINGAR:
1. **Alla längd-parametrar** ÷ 4
2. **TP/SL procentsatser** ÷ 3-4
3. **ATR-perioder** ÷ 4
4. **Smoothing-faktorer** ÷ 4

### TIPS FÖR 15MIN TRADING:
- ✅ Högre trade-frekvens (1+ trades/dag)
- ✅ Snabbare reaktion på marknadsrörelser
- ⚠️ Mer brus - kräver bättre filtrering
- ⚠️ Högre commission impact
- ⚠️ Kräver tightare risk management

### REKOMMENDATIONER:
1. Testa först med små positioner
2. Justera DPT-parametrarna för volatilitet
3. Överväg att öka "ActivateOrders" från 11 till 9-10 för fler trades
4. Använd BBFlipFinal för chop-markets
5. Aktivera ESPF och MESA modules

---

Skapad: 2026-01-17
För: Gypsy Bot v1.3
Timeframe: 15 minuter

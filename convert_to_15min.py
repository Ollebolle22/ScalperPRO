#!/usr/bin/env python3
"""
Gypsy Bot - Automatisk konvertering från 1H till 15min timeframe
Skapad: 2026-01-17
"""

import re

def convert_to_15min(input_file, output_file):
    """Konverterar Gypsy Bot-kod från 1H till 15min timeframe"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dictionary med alla ändringar (original_value: new_value)
    replacements = [
        # === GUPPY MMA LENGTHS ===
        ('ma1SPI = 3', 'ma1SPI = 1'),
        ('ma2SPI = 6', 'ma2SPI = 2'),
        ('ma3SPI = 9', 'ma3SPI = 2'),
        ('ma4SPI = 12', 'ma4SPI = 3'),
        ('ma5SPI = 15', 'ma5SPI = 4'),
        ('ma6SPI = 18', 'ma6SPI = 5'),
        ('ma7SPI = 21', 'ma7SPI = 5'),
        ('ma8SPI = 24', 'ma8SPI = 6'),
        ('ma9SPI = 27', 'ma9SPI = 7'),
        ('ma10SPI = 30', 'ma10SPI = 8'),
        ('ma11SPI = 33', 'ma11SPI = 8'),
        ('ma12SPI = 36', 'ma12SPI = 9'),
        ('ma13SPI = 39', 'ma13SPI = 10'),
        ('ma14SPI = 42', 'ma14SPI = 11'),
        ('ma15SPI = 45', 'ma15SPI = 11'),
        ('ma16SPI = 48', 'ma16SPI = 12'),
        ('ma17SPI = 51', 'ma17SPI = 13'),
        ('ma18SPI = 54', 'ma18SPI = 14'),
        ('ma19SPI = 57', 'ma19SPI = 14'),
        ('ma20SPI = 60', 'ma20SPI = 15'),
        ('ma21SPI = 63', 'ma21SPI = 16'),
        ('ma22SPI = 66', 'ma22SPI = 17'),
        ('ma23SPI = 200', 'ma23SPI = 50'),

        # === TSI ===
        ('longTSI = 25', 'longTSI = 6'),
        ('shortTSI = 13', 'shortTSI = 3'),
        ('signalTSI = 50', 'signalTSI = 12'),
        ('sig1smoother = ta.ema(sig1SPI, 14)', 'sig1smoother = ta.ema(sig1SPI, 4)'),
        ('sig2smoother = ta.ema(sig2SPI, 5)', 'sig2smoother = ta.ema(sig2SPI, 1)'),
        ('SSGuppy = ta.ema(sig1smoother, 4000)', 'SSGuppy = ta.ema(sig1smoother, 1000)'),

        # === HSRS ===
        ('lengthHSRS = 1000', 'lengthHSRS = 250'),
        ('nm_HSRS = 21', 'nm_HSRS = 5'),

        # === RISK MANAGEMENT - TP/SL ===
        ("tsActivationPre = input.float(18.0, 'Trailing Stop Activation (%)', minval = 0, step = 0.1, group = TSMod) / 100",
         "tsActivationPre = input.float(4.5, 'Trailing Stop Activation (%)', minval = 0, step = 0.1, group = TSMod) / 100"),
        ("tsPre = input.float(6.0, 'Trailing Stop (%)', minval = 0, step = 0.1, group = TSMod) / 100",
         "tsPre = input.float(1.5, 'Trailing Stop (%)', minval = 0, step = 0.1, group = TSMod) / 100"),
        ("tp = input.float(12.0, 'Take Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100",
         "tp = input.float(3.0, 'Take Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100"),
        ("ttp = input.float(2.5, 'Trailing Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100",
         "ttp = input.float(0.6, 'Trailing Profit (%)', minval = 0, step = 0.1, group = TakeProfitMod) / 100"),
        ("slPre = input.float(18.0, 'Stop Loss (%)', minval = 0, step = 0.1, group = SLMod) / 100",
         "slPre = input.float(4.5, 'Stop Loss (%)', minval = 0, step = 0.1, group = SLMod) / 100"),

        # === STAGED TAKE PROFITS ===
        ("Stp1Per = input.float(10.0, '1st Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp1Per = input.float(2.5, '1st Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)"),
        ("Stp1Trail = input.float(5.0, '1st Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp1Trail = input.float(1.2, '1st Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)"),
        ("Stp2Per = input.float(20.0, '2nd Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp2Per = input.float(5.0, '2nd Level - Take Profit Activation Percent (%))', minval = 0, step = 0.1, group = StagedTPMod)"),
        ("Stp2Trail = input.float(10.0, '2nd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp2Trail = input.float(2.5, '2nd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)"),
        ("Stp3Per = input.float(30.0, '3rd Level - Take Profit Activation Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp3Per = input.float(7.5, '3rd Level - Take Profit Activation Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)"),
        ("Stp3Trail = input.float(5.0, '3rd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)",
         "Stp3Trail = input.float(1.2, '3rd Level - Trailing Profit Percent (%)', minval = 0, step = 0.1, group = StagedTPMod)"),

        # === DCA ===
        ("DCA = input.float(1.0, 'DCA Threshold(%)', minval = 0, step = 0.1, group = DCAMod) / 100",
         "DCA = input.float(0.25, 'DCA Threshold(%)', minval = 0, step = 0.1, group = DCAMod) / 100"),

        # === ADX ===
        ("ADXlen = input.int(25, minval = 1, title = 'ADX DI Length', group = TEADX)",
         "ADXlen = input.int(6, minval = 1, title = 'ADX DI Length', group = TEADX)"),
        ('ADXlensig = 14', 'ADXlensig = 4'),
        ('ADXlenDPT = 4', 'ADXlenDPT = 1'),
        ("ADXThreshold = input(10, title = 'Primary Order Activation Threshold (Default = 10)', group = TEADX)",
         "ADXThreshold = input(8, title = 'Primary Order Activation Threshold (Default = 8)', group = TEADX)"),
        ("ADXSepThreshold = input(8, title = 'Secondary Order Activation Threshold (Default = 8)', group = TEADX)",
         "ADXSepThreshold = input(6, title = 'Secondary Order Activation Threshold (Default = 6)', group = TEADX)"),

        # === RSI MODULES ===
        ("Slength = input(7, 'Fast RSI Length', group = RSIMOD)",
         "Slength = input(2, 'Fast RSI Length', group = RSIMOD)"),
        ("SlengthSlow = input(35, 'Slow RSI Length', group = RSIMOD)",
         "SlengthSlow = input(9, 'Slow RSI Length', group = RSIMOD)"),
        ("lengthQQE = input.int(14, 'QQE Module - RSI Length', minval = 1, group = RSIMOD)",
         "lengthQQE = input.int(4, 'QQE Module - RSI Length', minval = 1, group = RSIMOD)"),

        # === MODULE 1 - MSA ===
        ("MASLength = input.int(14, 'Modified Slope Angle - Length (Default=14)', minval = 0, group = TEMod1)",
         "MASLength = input.int(4, 'Modified Slope Angle - Length (Default=4)', minval = 0, group = TEMod1)"),

        # === MODULE 2 - CTI ===
        ('LengthCTI = 14', 'LengthCTI = 4'),

        # === MODULE 3 - ERF ===
        ('highpassLengthERF = 48', 'highpassLengthERF = 12'),
        ('ssfLengthERF = 17', 'ssfLengthERF = 4'),

        # === MODULE 4 - Forecast ===
        ('lengthFO = 14', 'lengthFO = 4'),

        # === MODULE 5 - Chandelier ===
        ('Lengthz = 22', 'Lengthz = 6'),
        ('ATRPeriod = 22', 'ATRPeriod = 6'),
        ("windowBBQ = input(title = 'Bull Bear Qualifier - Lookback Window:', defval = 7, group = TEMod5)",
         "windowBBQ = input(title = 'Bull Bear Qualifier - Lookback Window:', defval = 2, group = TEMod5)"),

        # === MODULE 6 - CMB ===
        ('CMBmovingAverageLength1 = 20', 'CMBmovingAverageLength1 = 5'),
        ('CMBmovingAverageLength2 = 50', 'CMBmovingAverageLength2 = 12'),
        ('CMB_SmootherLength = 7', 'CMB_SmootherLength = 2'),

        # === MODULE 7 - DIC ===
        ('int fast_lengthDIC = 10', 'int fast_lengthDIC = 3'),
        ('int slow_lengthDICPRE = 2000', 'int slow_lengthDICPRE = 500'),

        # === MODULE 8 - MTI ===
        ("malen1 = input.int(defval = 14, title = 'MTI Agressive Length', minval = 1, group = TEMod8)",
         "malen1 = input.int(defval = 4, title = 'MTI Agressive Length', minval = 1, group = TEMod8)"),
        ("malen2 = input.int(defval = 35, title = 'MTI Normal Length', minval = 1, group = TEMod8)",
         "malen2 = input.int(defval = 9, title = 'MTI Normal Length', minval = 1, group = TEMod8)"),

        # === MODULE 9 - Ichimoku ===
        ('conversionPeriodsICHICLOUD = 9', 'conversionPeriodsICHICLOUD = 2'),
        ('basePeriodsICHICLOUD = 26', 'basePeriodsICHICLOUD = 7'),
        ('laggingSpan2PeriodsICHICLOUD = 52', 'laggingSpan2PeriodsICHICLOUD = 13'),
        ('displacementICHICLOUD = 26', 'displacementICHICLOUD = 7'),

        # === MODULE 10 - Harmonic ===
        ('lenHO = 14', 'lenHO = 4'),

        # === MODULE 11 - HSRS Compression ===
        ("lengthComp = input.int(21, title = 'HSRS Compression Length', minval = 1, group = TEMod11)",
         "lengthComp = input.int(5, title = 'HSRS Compression Length', minval = 1, group = TEMod11)"),

        # === MODULE 11 - Super AO ===
        ("AOfastLength = input(title = 'AO Fast Length', defval = 14)",
         "AOfastLength = input(title = 'AO Fast Length', defval = 4)"),
        ("AOslowLength = input(title = 'AO Slow Length', defval = 500)",
         "AOslowLength = input(title = 'AO Slow Length', defval = 125)"),
        ("AOSmoothInput = input(title = 'AO Smoother length', defval = 21)",
         "AOSmoothInput = input(title = 'AO Smoother length', defval = 5)"),
        ("STPeriods = input(title = 'ST ATR Period', defval = 14)",
         "STPeriods = input(title = 'ST ATR Period', defval = 4)"),

        # === MODULE 12 - Fisher Transform ===
        ('lengthFTMTF = 10', 'lengthFTMTF = 3'),

        # === DPT MTI Kicker ===
        ("KickerPercentUpTrendPre = input.float(2.0, 'MTI Kicker Activation (%) - Up Trend', minval = 0, step = 0.1, group = DPTMod)",
         "KickerPercentUpTrendPre = input.float(0.5, 'MTI Kicker Activation (%) - Up Trend', minval = 0, step = 0.1, group = DPTMod)"),
        ("KickerPercentDnTrend = input.float(6.0, 'MTI Kicker Activation (%) - Down Trend', minval = 0, step = 0.1, group = DPTMod)",
         "KickerPercentDnTrend = input.float(1.5, 'MTI Kicker Activation (%) - Down Trend', minval = 0, step = 0.1, group = DPTMod)"),

        # === ESPF ===
        ('fastLengthESPF = 40', 'fastLengthESPF = 10'),
        ('slowLengthESPF = 60', 'slowLengthESPF = 15'),

        # === Bollinger Bands ===
        ('lengthMBB = 34', 'lengthMBB = 8'),

        # === BB MESA Trading ===
        ("BBtsActivate = input.float(2.0, 'MESA ONLY - Trailing Stop Activation (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100",
         "BBtsActivate = input.float(0.5, 'MESA ONLY - Trailing Stop Activation (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100"),
        ("tsbb = input.float(1.0, 'Trailing Stop (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100",
         "tsbb = input.float(0.25, 'Trailing Stop (%)', minval = 0, step = 0.1, group = MesaTSMod) / 100"),

        # === ATS ===
        ('lenEMA = 50', 'lenEMA = 12'),

        # === RSI Stop ===
        ('rsi_maRSIS = McGinleyRSIS(close, 14)', 'rsi_maRSIS = McGinleyRSIS(close, 4)'),
        ('ATRRSIS = ta.atr(27)', 'ATRRSIS = ta.atr(7)'),

        # === DPT Components ===
        ('basePeriodsKJBB = 14', 'basePeriodsKJBB = 4'),
        ('displacementKJBB = 14', 'displacementKJBB = 4'),
        ('BB_lengthKJBB = 7', 'BB_lengthKJBB = 2'),
        ('st_periodSZ = 30', 'st_periodSZ = 8'),
        ('clenLRS = 50', 'clenLRS = 12'),
        ('slenLRS = 5', 'slenLRS = 1'),
        ('glenLRS = 13', 'glenLRS = 3'),

        # === Pi Cycle ===
        ('ln_ma_bottomlong = 471', 'ln_ma_bottomlong = 118'),
        ('ln_ma_bottomshort = 150', 'ln_ma_bottomshort = 38'),

        # === Strategy Title ===
        ("strategy('Gyspy Bot Trade Engine - V1.2B - Strategy 12-7-25'",
         "strategy('Gyspy Bot Trade Engine - V1.3 - 15MIN - Strategy 01-17-26'"),
    ]

    # Utför alla ersättningar
    for old, new in replacements:
        content = content.replace(old, new)

    # Skriv till output-fil
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Konvertering klar!")
    print(f"📁 Input:  {input_file}")
    print(f"📁 Output: {output_file}")
    print(f"🔧 Totalt {len(replacements)} parametrar justerade för 15min timeframe")

if __name__ == '__main__':
    input_file = 'GypsyEmil.pine'
    output_file = 'GypsyEmil_15MIN.pine'

    convert_to_15min(input_file, output_file)

    print("\n📋 Nästa steg:")
    print("1. Öppna GypsyEmil_15MIN.pine i TradingView")
    print("2. Testa på 15-minuters chart")
    print("3. Justera ActivateOrders från 11 till 9-10 för fler trades")
    print("4. Backtesta noggrant innan live trading")
    print("\n⚠️  VIKTIGT: Börja med små positioner!")

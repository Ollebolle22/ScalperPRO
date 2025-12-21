# ⚡ Momentum Scalper PRO v8.0 - 15M Optimized

> Professional momentum scalping strategy optimized for 15-minute timeframe crypto trading

## 🎯 Snabb Start

### Installation i TradingView

1. **Öppna TradingView**
   - Gå till din 15-minuters chart (SOL/USDC rekommenderas)

2. **Ladda upp strategin**
   - Pine Editor → New → Kopiera innehållet från `Scalper_Optimized_15M.pine`
   - Save → Add to Chart

3. **Konfigurera Settings**
   ```
   Leverage: 5.0 (börja med 3.0 för säkerhet)
   ADX Filter: ON (kritiskt!)
   Partial TP: ON
   Trailing Stop: ON
   Session Filter: ON (0800-2200)
   ```

4. **Koppla till Bot** (valfritt)
   - Bot ID: Din WunderTrading bot ID
   - Exchange: HyperLiquid/Binance/Bybit
   - Pair: SOL-USDC (eller din pair)
   - Skapa Alerts för alla signals

---

## 📊 Vad är nytt i v8.0?

### 🔥 Största Förbättringar

1. **ADX Trend Filter** - Filtrerar ranging markets (ADX <25)
2. **Partial Take Profit** - Låser 50% vinst vid 1.5R
3. **Fixad Trailing Stop** - Korrekt implementation (aktiveras vid 2R)
4. **Bättre R:R** - 2:1 istället för 1.5:1 (TP=5.0 ATR, SL=2.5 ATR)
5. **Striktare Entry** - Färre men bättre trades
6. **15min-specifika parametrar** - EMA 21/50/100, ATR 20, Vol 1.5x

### 📈 Förväntade Resultat

| Metric | Target |
|--------|--------|
| Win Rate | **50-55%** |
| Profit Factor | **1.8-2.5** |
| Avg R:R | **2.0+** |
| Max Drawdown | **10-15%** |
| Trades/månad | **30-50** |

---

## ⚙️ Rekommenderade Inställningar per Stil

### 🛡️ Konservativ (Rekommenderad för nybörjare)
```
💰 Kapital & Leverage:
   - Leverage: 3.0
   - Liq Buffer: 40%
   - Position Size: 80%

🔄 DCA:
   - Aktivera DCA: NO

💪 ADX:
   - ADX Minimum: 30

🎯 Risk:
   - Partial TP: ON (50% @ 1.5R)
   - Trailing: ON (aktivera @ 2.0R)
   - Breakeven: ON (@ 1.2R)
```

### ⚡ Balanserad (Default - Rekommenderad)
```
💰 Kapital & Leverage:
   - Leverage: 5.0
   - Liq Buffer: 30%
   - Position Size: 95%

🔄 DCA:
   - Aktivera DCA: YES
   - Max entries: 2
   - Mode: ATR Smart (2.5x)
   - Require Trend: YES

💪 ADX:
   - ADX Minimum: 25

🎯 Risk:
   - ATR SL Mult: 2.5
   - ATR TP Mult: 5.0
   - Partial TP: ON
```

### 🚀 Aggressiv (Erfarna traders)
```
💰 Kapital & Leverage:
   - Leverage: 7.0-10.0
   - Liq Buffer: 25%
   - Position Size: 100%

🔄 DCA:
   - Max entries: 3
   - DCA Size Mult: 1.5

💪 ADX:
   - ADX Minimum: 20

🎯 Risk:
   - Partial TP: 30% @ 1.5R
   - Trailing: ON (aktivera @ 1.5R, offset 1.0 ATR)
```

---

## 📋 Filters & Indicators

### Aktiva Filters (Standard)

✅ **EMA Trend Filter** - EMA 21 > EMA 50 för long
✅ **ADX Strength** - ADX ≥25 (filtrerar ranging)
✅ **RSI Zone** - Long: 45-65, Short: 35-55
✅ **MACD Cross** - Kräver faktisk korsning
✅ **Volume** - 1.5x över 24-bar MA
✅ **Session** - 08:00-22:00 CET
✅ **EMA Spacing** - Min 0.3% separation

### När Tar Man Trades?

**LONG Entry när:**
```
✓ EMA 21 korsar över EMA 50
✓ Pris över EMA 100
✓ MACD korsar över signal-linje
✓ MACD histogram ökar
✓ RSI mellan 45-65
✓ ADX ≥25
✓ Volym >1.5x genomsnitt
✓ Inom trading session (08-22)
✓ EMAs separerade ≥0.3%
```

**SHORT Entry:** Motsatt

---

## 🎨 Chart Setup Guide

### Rekommenderad Layout

**Main Chart (15min):**
- Strategin med alla EMAs (blå/orange/lila)
- Info Panel (top right)
- Trade labels

**Sub-charts:**
1. **RSI (14)** - Se overbought/oversold
2. **MACD (12,26,9)** - Bekräfta crossovers
3. **ADX (14)** - Verifiera trend strength
4. **Volume** - Bekräfta breakouts

### Färgschema (Default)

- **Fast EMA (21):** Blå
- **Slow EMA (50):** Orange
- **Trend EMA (100):** Lila
- **Bullish:** Grön (#26A69A)
- **Bearish:** Röd (#EF5350)
- **Stop Loss:** Röd
- **Take Profit:** Grön
- **Partial TP:** Orange
- **Liquidation:** Magenta

---

## 🤖 Bot Integration (WunderTrading)

### Alert Setup

1. **Skapa Alerts i TradingView**
   - Högerklicka på chart → Add Alert
   - Condition: Strategy alert (Scalper v8.0)
   - Alert name: "SOL 15M - {{strategy.order.action}}"

2. **Webhook URL** (WunderTrading)
   ```
   https://api.wundertrading.com/v1/webhook/your-webhook-id
   ```

3. **Alert Message** (automatisk från strategy)
   ```json
   {
     "code": "ENTER-LONG_HyperLiquid_SOL-USDC_SOL_15M_botid",
     "price": "123.45",
     "sl": "120.00",
     "tp": "130.00",
     "type": "ENTRY"
   }
   ```

### Bot Settings i Strategy

```pinescript
Bot ID: Din WunderTrading bot ID
Exchange: HyperLiquid (eller Binance/Bybit/OKX)
Pair: SOL-USDC
Strategy Name: SOL_15M
```

---

## 📊 Info Panel Guide

### Market Section
- **Trend:** Bullish/Bearish/Neutral
- **ADX:** Trend strength (💪 STARK när >35)
- **RSI:** Current value med färgkodning
- **MACD:** Bull/Bear + histogram riktning
- **Volume:** High/Low jämfört med MA

### Position Section
- **Status:** Long/Short/Flat
- **Entry:** Genomsnittligt entry-pris
- **Current R:** Nuvarande risk-multipel
- **P&L:** % vinst/förlust (inkl leverage)
- **Stop Loss:** Aktuell SL (🔒 = breakeven)
- **Take Profit:** Full TP-nivå
- **Partial TP:** Partial TP-pris eller ✅ om tagen
- **Trailing:** Status (🔥 ACTIVE eller ⏳ Wait X.XR)
- **Liq Dist:** Avstånd till likvidation i %
- **DCA:** Antal entries (1/2)

### Performance Section
- **Trades:** Totalt antal stängda trades
- **Win Rate:** % vinnande trades
- **Profit Factor:** Gross profit / Gross loss
- **Avg R:R:** Genomsnittlig risk:reward
- **Net P&L:** Total vinst/förlust i $

---

## 🛠️ Troubleshooting

### "För många trades"
→ Öka `adxThreshold` till 30
→ Sänk `emaSpacing` till 0.5%
→ Aktivera `requireMACDCross`

### "För få trades"
→ Sänk `adxThreshold` till 20
→ Öka `rsiLongMax` till 70
→ Sänk `volMultiplier` till 1.3

### "För många stop-outs"
→ Öka `atrMultSL` till 3.0
→ Aktivera `useBreakeven`
→ Kontrollera att ADX-filter är ON

### "Trades går inte till TP"
→ Sänk `atrMultTP` till 4.0
→ Använd Partial TP (50% @ 1.5R)
→ Aktivera trailing stop

### "Bot får inga alerts"
→ Kontrollera att Alert är created i TradingView
→ Verifiera Webhook URL
→ Testa med manual alert först
→ Kontrollera att `bot_id` är korrekt

---

## 📈 Backtesting Guide

### Steg 1: Initial Test
```
Timeframe: 15min
Asset: SOL/USDC
Period: Senaste 6 månader
Initial Capital: $10,000
```

### Steg 2: Analysera Metrics
Godkänd om:
- ✅ Win Rate >45%
- ✅ Profit Factor >1.5
- ✅ Max Drawdown <20%
- ✅ Net Profit >0

### Steg 3: Optimera
Om metrics är dåliga:
1. Kontrollera ADX är ON
2. Öka `emaFastLen` till 25
3. Öka `volMultiplier` till 1.7
4. Öka `adxThreshold` till 28

### Steg 4: Walk-Forward Test
- Test på 3 månader
- Trade på 1 månad
- Repetera

---

## ⚠️ Risk Disclaimer

**VARNINGAR:**

1. **Leverage är riskabelt**
   - 5x leverage = 5x vinster MEN också 5x förluster
   - Kan förlora mer än initial capital
   - Börja alltid lågt (3x)

2. **Backtesting ≠ Live Results**
   - Funding rates inte inkluderade
   - Slippage kan vara högre
   - Market conditions ändras

3. **Never risk more than 2% per trade**
   - Med 5x leverage = max 10% av equity per position
   - Använd position sizing wisely

4. **Crypto är volatilt**
   - 50% swings är normalt
   - Black swan events händer
   - Ha alltid emergency exit plan

**REKOMMENDATION:** Paper trade i 2 veckor innan live.

---

## 🎓 Learning Resources

### Förstå Indicators
- **EMA:** https://tradingview.com/support/solutions/43000502589
- **ADX:** https://tradingview.com/support/solutions/43000501969
- **MACD:** https://tradingview.com/support/solutions/43000502344
- **RSI:** https://tradingview.com/support/solutions/43000502338

### Risk Management
- Position sizing calculators
- Kelly Criterion
- R-multiples

---

## 📞 Support & Updates

**Fil struktur:**
```
ScalperPRO/
├── Scalper.pine                    # Original v7.5
├── Scalper_Optimized_15M.pine     # NYA v8.0 (ANVÄND DENNA!)
├── CHANGELOG_v8.0.md              # Alla ändringar
├── README_v8.0.md                 # Denna fil
└── README.md                      # Original README
```

**Frågor?**
- Läs CHANGELOG_v8.0.md för detaljer
- Kontrollera Troubleshooting-sektionen
- Testa i Paper Trading först

---

## ✅ Quick Checklist innan Live Trading

- [ ] Backtested på minst 6 månader data
- [ ] Paper traded i 2 veckor
- [ ] Förstår alla parametrar
- [ ] Alert setup och testat
- [ ] Bot integration verifierad
- [ ] Risk management på plats (max 2% per trade)
- [ ] Emergency exit plan
- [ ] Börjar med låg leverage (3x)
- [ ] Börjar med 5-10% av total capital
- [ ] Monitoring setup (daglig check)

---

**Version:** 8.0
**Optimerad för:** 15-minute timeframe
**Rekommenderade pairs:** SOL/USDC, BTC/USD, ETH/USD
**Leverage:** 3-5x (max 10x för erfarna)

**Lycka till! 🚀📈**

*"The trend is your friend until the end when it bends."*

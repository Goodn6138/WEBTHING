<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Health Monitor - Height, Weight & Wellness</title>

  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-primary: #0f172a;
      --bg-card: #1e293b;
      --bg-card-hover: #243447;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent-primary: #3b82f6;
      --accent-secondary: #06b6d4;
      --accent-success: #10b981;
      --accent-warning: #f59e0b;
      --accent-danger: #ef4444;
      --accent-purple: #8b5cf6;
      --border-color: #334155;
      --shadow-glow: 0 0 20px rgba(59, 130, 246, 0.15);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg-primary);
      color: var(--text-primary);
      min-height: 100vh;
      padding: 20px;
      overflow-x: hidden;
    }

    /* Animated background particles */
    .bg-animation {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .bg-animation .particle {
      position: absolute;
      width: 4px;
      height: 4px;
      background: var(--accent-primary);
      border-radius: 50%;
      opacity: 0.3;
      animation: float 15s infinite ease-in-out;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0) translateX(0); opacity: 0.3; }
      25% { transform: translateY(-30px) translateX(20px); opacity: 0.6; }
      50% { transform: translateY(-20px) translateX(-20px); opacity: 0.4; }
      75% { transform: translateY(-40px) translateX(10px); opacity: 0.5; }
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }

    /* Header */
    .header {
      text-align: center;
      margin-bottom: 40px;
      padding-top: 20px;
    }

    .header h1 {
      font-size: 2.5rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-primary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 8px;
    }

    .header p {
      color: var(--text-secondary);
      font-size: 1.1rem;
      font-weight: 300;
    }

    .last-updated {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-top: 12px;
      padding: 6px 16px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 20px;
      font-size: 0.85rem;
      color: var(--accent-success);
    }

    .last-updated .dot {
      width: 8px;
      height: 8px;
      background: var(--accent-success);
      border-radius: 50%;
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(0.8); }
    }

    /* Grid Layout */
    .dashboard-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      margin-bottom: 30px;
    }

    /* Card Base */
    .card {
      background: var(--bg-card);
      border-radius: 20px;
      padding: 28px;
      border: 1px solid var(--border-color);
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }

    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .card:hover {
      transform: translateY(-4px);
      background: var(--bg-card-hover);
      box-shadow: var(--shadow-glow);
      border-color: rgba(59, 130, 246, 0.3);
    }

    .card:hover::before {
      opacity: 1;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
    }

    .card-title {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .card-icon {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }

    .card-icon.blue { background: rgba(59, 130, 246, 0.15); color: var(--accent-primary); }
    .card-icon.cyan { background: rgba(6, 182, 212, 0.15); color: var(--accent-secondary); }
    .card-icon.green { background: rgba(16, 185, 129, 0.15); color: var(--accent-success); }
    .card-icon.orange { background: rgba(245, 158, 11, 0.15); color: var(--accent-warning); }
    .card-icon.purple { background: rgba(139, 92, 246, 0.15); color: var(--accent-purple); }
    .card-icon.red { background: rgba(239, 68, 68, 0.15); color: var(--accent-danger); }

    .card-value {
      font-size: 2.8rem;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1;
      margin-bottom: 8px;
    }

    .card-value .unit {
      font-size: 1rem;
      font-weight: 400;
      color: var(--text-muted);
      margin-left: 4px;
    }

    .card-subtitle {
      font-size: 0.9rem;
      color: var(--text-secondary);
    }

    /* BMI Card Special */
    .bmi-card {
      grid-column: span 2;
    }

    .bmi-display {
      display: flex;
      align-items: center;
      gap: 30px;
      margin: 20px 0;
    }

    .bmi-circle {
      position: relative;
      width: 140px;
      height: 140px;
      flex-shrink: 0;
    }

    .bmi-circle svg {
      transform: rotate(-90deg);
    }

    .bmi-circle-bg {
      fill: none;
      stroke: var(--border-color);
      stroke-width: 8;
    }

    .bmi-circle-progress {
      fill: none;
      stroke-width: 8;
      stroke-linecap: round;
      transition: stroke-dashoffset 1s ease;
    }

    .bmi-circle-text {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
    }

    .bmi-circle-text .number {
      font-size: 2rem;
      font-weight: 700;
      color: var(--text-primary);
    }

    .bmi-circle-text .label {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .bmi-info {
      flex: 1;
    }

    .bmi-status {
      display: inline-block;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      margin-bottom: 12px;
    }

    .bmi-status.underweight { background: rgba(59, 130, 246, 0.15); color: var(--accent-primary); }
    .bmi-status.normal { background: rgba(16, 185, 129, 0.15); color: var(--accent-success); }
    .bmi-status.overweight { background: rgba(245, 158, 11, 0.15); color: var(--accent-warning); }
    .bmi-status.obese { background: rgba(239, 68, 68, 0.15); color: var(--accent-danger); }

    .bmi-description {
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.6;
    }

    /* BMI Scale */
    .bmi-scale {
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid var(--border-color);
    }

    .scale-bar {
      position: relative;
      height: 12px;
      background: linear-gradient(90deg, 
        var(--accent-primary) 0%, 
        var(--accent-primary) 18.5%,
        var(--accent-success) 18.5%, 
        var(--accent-success) 25%,
        var(--accent-warning) 25%, 
        var(--accent-warning) 30%,
        var(--accent-danger) 30%, 
        var(--accent-danger) 100%
      );
      border-radius: 6px;
      margin-bottom: 8px;
    }

    .scale-marker {
      position: absolute;
      top: -6px;
      width: 24px;
      height: 24px;
      background: white;
      border: 3px solid var(--accent-primary);
      border-radius: 50%;
      transform: translateX(-50%);
      transition: left 0.5s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }

    .scale-labels {
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    /* BMR Card */
    .bmr-card {
      grid-column: span 2;
    }

    .bmr-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin: 20px 0;
    }

    .bmr-stat {
      text-align: center;
      padding: 16px;
      background: rgba(255,255,255,0.03);
      border-radius: 12px;
      border: 1px solid var(--border-color);
    }

    .bmr-stat .value {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 4px;
    }

    .bmr-stat .label {
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Activity Section */
    .activity-card {
      grid-column: span 2;
    }

    .activity-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }

    .activity-item {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 16px;
      background: rgba(255,255,255,0.03);
      border-radius: 12px;
      border: 1px solid var(--border-color);
      transition: all 0.2s ease;
    }

    .activity-item:hover {
      background: rgba(255,255,255,0.05);
      border-color: var(--accent-primary);
    }

    .activity-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      flex-shrink: 0;
    }

    .activity-details h4 {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 2px;
    }

    .activity-details p {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Wellness Advice */
    .advice-card {
      grid-column: span 2;
    }

    .advice-tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    .advice-tab {
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: transparent;
      color: var(--text-secondary);
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .advice-tab:hover {
      border-color: var(--accent-primary);
      color: var(--text-primary);
    }

    .advice-tab.active {
      background: var(--accent-primary);
      border-color: var(--accent-primary);
      color: white;
    }

    .advice-content {
      display: none;
    }

    .advice-content.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .advice-list {
      list-style: none;
    }

    .advice-list li {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 14px 0;
      border-bottom: 1px solid var(--border-color);
    }

    .advice-list li:last-child {
      border-bottom: none;
    }

    .advice-list .bullet {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .advice-list .bullet.green { background: rgba(16, 185, 129, 0.15); color: var(--accent-success); }
    .advice-list .bullet.blue { background: rgba(59, 130, 246, 0.15); color: var(--accent-primary); }
    .advice-list .bullet.orange { background: rgba(245, 158, 11, 0.15); color: var(--accent-warning); }
    .advice-list .bullet.purple { background: rgba(139, 92, 246, 0.15); color: var(--accent-purple); }

    .advice-list .text {
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.5;
    }

    .advice-list .text strong {
      color: var(--text-primary);
      font-weight: 600;
    }

    /* Trend Chart */
    .trend-card {
      grid-column: span 2;
    }

    .chart-container {
      position: relative;
      height: 200px;
      margin-top: 20px;
    }

    .chart-svg {
      width: 100%;
      height: 100%;
    }

    .chart-line {
      fill: none;
      stroke: var(--accent-primary);
      stroke-width: 3;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .chart-area {
      fill: rgba(59, 130, 246, 0.1);
    }

    .chart-dot {
      fill: var(--bg-card);
      stroke: var(--accent-primary);
      stroke-width: 3;
    }

    .chart-grid {
      stroke: var(--border-color);
      stroke-width: 1;
      stroke-dasharray: 4,4;
    }

    .chart-label {
      fill: var(--text-muted);
      font-size: 11px;
      text-anchor: middle;
    }

    /* Footer */
    .footer {
      text-align: center;
      padding: 30px 0;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    .footer a {
      color: var(--accent-primary);
      text-decoration: none;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .header h1 { font-size: 1.8rem; }
      .dashboard-grid { grid-template-columns: 1fr; }
      .bmi-card, .bmr-card, .activity-card, .advice-card, .trend-card { grid-column: span 1; }
      .bmi-display { flex-direction: column; text-align: center; }
      .bmr-stats { grid-template-columns: 1fr; }
      .card-value { font-size: 2.2rem; }
    }

    /* Loading shimmer */
    .shimmer {
      background: linear-gradient(90deg, var(--bg-card) 25%, #2a3a4f 50%, var(--bg-card) 75%);
      background-size: 200% 100%;
      animation: shimmer 1.5s infinite;
      border-radius: 8px;
      color: transparent !important;
    }

    @keyframes shimmer {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    /* Connection status */
    .connection-status {
      position: fixed;
      top: 20px;
      right: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      font-size: 0.8rem;
      z-index: 100;
      transition: all 0.3s ease;
    }

    .connection-status.online {
      border-color: rgba(16, 185, 129, 0.3);
      color: var(--accent-success);
    }

    .connection-status.offline {
      border-color: rgba(239, 68, 68, 0.3);
      color: var(--accent-danger);
    }

    .connection-status .indicator {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      animation: pulse 2s infinite;
    }

    .connection-status.online .indicator { background: var(--accent-success); }
    .connection-status.offline .indicator { background: var(--accent-danger); animation: none; }
  </style>
<base target="_blank">
</head>

<body>
  <!-- Background Animation -->
  <div class="bg-animation" id="bgAnimation"></div>

  <!-- Connection Status -->
  <div class="connection-status online" id="connectionStatus">
    <div class="indicator"></div>
    <span>Live Data</span>
  </div>

  <div class="container">
    <!-- Header -->
    <div class="header">
      <h1>Health Monitor</h1>
      <p>Track your vitals, calculate metrics, and get personalized wellness advice</p>
      <div class="last-updated">
        <div class="dot"></div>
        <span id="lastUpdated">Last updated: Just now</span>
      </div>
    </div>

    <!-- Dashboard Grid -->
    <div class="dashboard-grid">

      <!-- Height Card -->
      <div class="card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon blue">📏</div>
            Height
          </div>
        </div>
        <div class="card-value" id="heightValue">
          <span class="shimmer" style="display:inline-block;width:80px;height:40px;">&nbsp;</span>
        </div>
        <div class="card-subtitle">Current measurement</div>
      </div>

      <!-- Weight Card -->
      <div class="card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon cyan">⚖️</div>
            Weight
          </div>
        </div>
        <div class="card-value" id="weightValue">
          <span class="shimmer" style="display:inline-block;width:80px;height:40px;">&nbsp;</span>
        </div>
        <div class="card-subtitle">Current measurement</div>
      </div>

      <!-- Age Card (placeholder for future data) -->
      <div class="card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon purple">🎂</div>
            Age
          </div>
        </div>
        <div class="card-value" id="ageValue">
          <span class="shimmer" style="display:inline-block;width:60px;height:40px;">&nbsp;</span>
        </div>
        <div class="card-subtitle">Used for BMR calculation</div>
      </div>

      <!-- Gender Card (placeholder for future data) -->
      <div class="card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon orange">👤</div>
            Gender
          </div>
        </div>
        <div class="card-value" id="genderValue" style="font-size: 1.5rem;">
          <span class="shimmer" style="display:inline-block;width:80px;height:40px;">&nbsp;</span>
        </div>
        <div class="card-subtitle">Used for BMR calculation</div>
      </div>

      <!-- BMI Card -->
      <div class="card bmi-card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon green">📊</div>
            Body Mass Index (BMI)
          </div>
        </div>
        <div class="bmi-display">
          <div class="bmi-circle">
            <svg width="140" height="140" viewBox="0 0 140 140">
              <circle class="bmi-circle-bg" cx="70" cy="70" r="60"/>
              <circle class="bmi-circle-progress" id="bmiProgress" cx="70" cy="70" r="60"
                stroke="var(--accent-primary)"
                stroke-dasharray="377"
                stroke-dashoffset="377"/>
            </svg>
            <div class="bmi-circle-text">
              <div class="number" id="bmiNumber">--</div>
              <div class="label">BMI</div>
            </div>
          </div>
          <div class="bmi-info">
            <div class="bmi-status" id="bmiStatus">Calculating...</div>
            <p class="bmi-description" id="bmiDescription">
              BMI is calculated using your height and weight to assess if you're at a healthy weight for your height.
            </p>
          </div>
        </div>
        <div class="bmi-scale">
          <div class="scale-bar">
            <div class="scale-marker" id="bmiMarker" style="left: 0%;"></div>
          </div>
          <div class="scale-labels">
            <span>Underweight<br>&lt;18.5</span>
            <span>Normal<br>18.5-24.9</span>
            <span>Overweight<br>25-29.9</span>
            <span>Obese<br>≥30</span>
          </div>
        </div>
      </div>

      <!-- BMR Card -->
      <div class="card bmr-card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon red">🔥</div>
            Basal Metabolic Rate (BMR)
          </div>
        </div>
        <div class="bmr-stats">
          <div class="bmr-stat">
            <div class="value" id="bmrValue">
              <span class="shimmer" style="display:inline-block;width:100px;height:36px;">&nbsp;</span>
            </div>
            <div class="label">Calories / Day</div>
          </div>
          <div class="bmr-stat">
            <div class="value" id="bmrSedentary">
              <span class="shimmer" style="display:inline-block;width:100px;height:36px;">&nbsp;</span>
            </div>
            <div class="label">Sedentary</div>
          </div>
          <div class="bmr-stat">
            <div class="value" id="bmrActive">
              <span class="shimmer" style="display:inline-block;width:100px;height:36px;">&nbsp;</span>
            </div>
            <div class="label">Moderately Active</div>
          </div>
        </div>
        <p class="card-subtitle" style="margin-top: 12px;">
          BMR represents the minimum calories your body needs at rest. Sedentary and Active values include activity multipliers.
        </p>
      </div>

      <!-- Physical Activity Card -->
      <div class="card activity-card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon green">🏃</div>
            Physical Activity
          </div>
        </div>
        <div class="activity-grid" id="activityGrid">
          <!-- Activities will be populated dynamically -->
          <div class="activity-item">
            <div class="activity-icon" style="background: rgba(59,130,246,0.15); color: var(--accent-primary);">🚶</div>
            <div class="activity-details">
              <h4>Steps Today</h4>
              <p id="stepsValue">Waiting for data...</p>
            </div>
          </div>
          <div class="activity-item">
            <div class="activity-icon" style="background: rgba(6,182,212,0.15); color: var(--accent-secondary);">⏱️</div>
            <div class="activity-details">
              <h4>Active Minutes</h4>
              <p id="activeMinutesValue">Waiting for data...</p>
            </div>
          </div>
          <div class="activity-item">
            <div class="activity-icon" style="background: rgba(16,185,129,0.15); color: var(--accent-success);">🔥</div>
            <div class="activity-details">
              <h4>Calories Burned</h4>
              <p id="caloriesBurnedValue">Waiting for data...</p>
            </div>
          </div>
          <div class="activity-item">
            <div class="activity-icon" style="background: rgba(139,92,246,0.15); color: var(--accent-purple);">💤</div>
            <div class="activity-details">
              <h4>Sleep Duration</h4>
              <p id="sleepValue">Waiting for data...</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Wellness Advice Card -->
      <div class="card advice-card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon blue">💡</div>
            Personalized Wellness Advice
          </div>
        </div>
        <div class="advice-tabs">
          <button class="advice-tab active" data-tab="nutrition">🍎 Nutrition</button>
          <button class="advice-tab" data-tab="physical">💪 Physical</button>
          <button class="advice-tab" data-tab="mental">🧠 Mental Health</button>
        </div>

        <div class="advice-content active" id="nutrition">
          <ul class="advice-list" id="nutritionAdvice">
            <li>
              <div class="bullet green">✓</div>
              <div class="text">Loading personalized nutrition advice...</div>
            </li>
          </ul>
        </div>

        <div class="advice-content" id="physical">
          <ul class="advice-list" id="physicalAdvice">
            <li>
              <div class="bullet blue">✓</div>
              <div class="text">Loading personalized physical activity advice...</div>
            </li>
          </ul>
        </div>

        <div class="advice-content" id="mental">
          <ul class="advice-list" id="mentalAdvice">
            <li>
              <div class="bullet purple">✓</div>
              <div class="text">Loading personalized mental health advice...</div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Trend Chart Card -->
      <div class="card trend-card">
        <div class="card-header">
          <div class="card-title">
            <div class="card-icon cyan">📈</div>
            Weight Trend (Last 7 Days)
          </div>
        </div>
        <div class="chart-container">
          <svg class="chart-svg" id="weightChart" viewBox="0 0 800 200" preserveAspectRatio="none">
            <!-- Grid lines -->
            <line class="chart-grid" x1="0" y1="50" x2="800" y2="50"/>
            <line class="chart-grid" x1="0" y1="100" x2="800" y2="100"/>
            <line class="chart-grid" x1="0" y1="150" x2="800" y2="150"/>
            <!-- Chart will be drawn by JS -->
          </svg>
        </div>
      </div>

    </div>

    <!-- Footer -->
    <div class="footer">
      <p>Health Monitor &copy; 2026 | Data refreshes automatically every second</p>
    </div>
  </div>

  <script>
    // =====================
    // BACKGROUND PARTICLES
    // =====================
    function createParticles() {
      const container = document.getElementById('bgAnimation');
      for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 15 + 's';
        particle.style.animationDuration = (10 + Math.random() * 10) + 's';
        container.appendChild(particle);
      }
    }
    createParticles();

    // =====================
    // STATE
    // =====================
    let currentData = {
      height: null,
      weight: null,
      age: 30,      // default fallback
      gender: 'male', // default fallback
      steps: 0,
      activeMinutes: 0,
      caloriesBurned: 0,
      sleepHours: 0,
      history: []
    };

    // Simulated history for demo (replace with real data from backend)
    const demoHistory = [
      { date: 'Mon', weight: 72.5 },
      { date: 'Tue', weight: 72.3 },
      { date: 'Wed', weight: 72.1 },
      { date: 'Thu', weight: 71.9 },
      { date: 'Fri', weight: 71.8 },
      { date: 'Sat', weight: 71.6 },
      { date: 'Sun', weight: 71.5 }
    ];

    // =====================
    // CALCULATIONS
    // =====================
    function calculateBMI(heightCm, weightKg) {
      if (!heightCm || !weightKg) return null;
      const heightM = heightCm / 100;
      return (weightKg / (heightM * heightM)).toFixed(1);
    }

    function getBMIStatus(bmi) {
      if (bmi < 18.5) return { status: 'underweight', text: 'Underweight', color: 'var(--accent-primary)' };
      if (bmi < 25) return { status: 'normal', text: 'Normal Weight', color: 'var(--accent-success)' };
      if (bmi < 30) return { status: 'overweight', text: 'Overweight', color: 'var(--accent-warning)' };
      return { status: 'obese', text: 'Obese', color: 'var(--accent-danger)' };
    }

    function getBMIDescription(bmi) {
      if (bmi < 18.5) return 'You are below the recommended weight range. Consider increasing your caloric intake with nutrient-dense foods and consult a healthcare provider.';
      if (bmi < 25) return 'Great job! Your BMI is within the healthy range. Maintain your current lifestyle with balanced nutrition and regular physical activity.';
      if (bmi < 30) return 'You are above the recommended weight range. Focus on portion control, increase physical activity, and consider consulting a nutritionist.';
      return 'Your BMI indicates obesity, which may increase health risks. It is recommended to consult a healthcare provider for a personalized weight management plan.';
    }

    function calculateBMR(weightKg, heightCm, age, gender) {
      if (!weightKg || !heightCm || !age) return null;
      // Mifflin-St Jeor Equation
      let bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age);
      if (gender === 'male') {
        bmr += 5;
      } else {
        bmr -= 161;
      }
      return Math.round(bmr);
    }

    // =====================
    // ADVICE GENERATION
    // =====================
    function generateAdvice(data) {
      const bmi = calculateBMI(data.height, data.weight);
      const advice = {
        nutrition: [],
        physical: [],
        mental: []
      };

      // Nutrition advice based on BMI
      if (bmi) {
        if (bmi < 18.5) {
          advice.nutrition.push(
            { icon: 'green', text: '<strong>Increase caloric intake:</strong> Add healthy snacks like nuts, avocados, and whole-grain toast with peanut butter between meals.' },
            { icon: 'blue', text: '<strong>Protein-rich foods:</strong> Include lean meats, fish, eggs, legumes, and dairy to support healthy weight gain and muscle building.' },
            { icon: 'orange', text: '<strong>Nutrient-dense smoothies:</strong> Blend bananas, oats, Greek yogurt, and honey for a calorie-rich, nutritious drink.' }
          );
        } else if (bmi < 25) {
          advice.nutrition.push(
            { icon: 'green', text: '<strong>Maintain balance:</strong> Continue with a varied diet including fruits, vegetables, whole grains, and lean proteins.' },
            { icon: 'blue', text: '<strong>Hydration:</strong> Drink at least 8 glasses of water daily. Proper hydration supports metabolism and energy levels.' },
            { icon: 'orange', text: '<strong>Portion awareness:</strong> Use smaller plates and eat mindfully to maintain your healthy weight long-term.' }
          );
        } else {
          advice.nutrition.push(
            { icon: 'green', text: '<strong>Reduce processed foods:</strong> Cut back on sugary drinks, fast food, and snacks high in saturated fats and sodium.' },
            { icon: 'blue', text: '<strong>Increase fiber:</strong> Eat more vegetables, fruits, and whole grains to stay full longer and support digestion.' },
            { icon: 'orange', text: '<strong>Lean protein focus:</strong> Choose chicken breast, fish, tofu, and legumes to maintain muscle while reducing calories.' }
          );
        }
      }

      // Physical activity advice
      if (data.steps < 5000) {
        advice.physical.push(
          { icon: 'green', text: '<strong>Start walking:</strong> Aim for a 15-minute walk after meals. Small steps lead to big changes in cardiovascular health.' },
          { icon: 'blue', text: '<strong>Take the stairs:</strong> Replace elevator rides with stair climbing to build leg strength and burn extra calories.' },
          { icon: 'orange', text: '<strong>Set a step goal:</strong> Try to reach 5,000 steps daily, then gradually increase to the recommended 10,000.' }
        );
      } else if (data.steps < 10000) {
        advice.physical.push(
          { icon: 'green', text: '<strong>Great progress!</strong> You are on your way to the 10,000 step goal. Try adding a brisk 20-minute walk to your routine.' },
          { icon: 'blue', text: '<strong>Add strength training:</strong> Incorporate bodyweight exercises like squats, push-ups, and planks twice a week.' },
          { icon: 'orange', text: '<strong>Mix it up:</strong> Try cycling, swimming, or dancing to keep your workouts fun and engaging.' }
        );
      } else {
        advice.physical.push(
          { icon: 'green', text: '<strong>Excellent activity level!</strong> You are exceeding the daily step recommendation. Maintain this momentum.' },
          { icon: 'blue', text: '<strong>Challenge yourself:</strong> Add interval training or hill walks to increase intensity and cardiovascular benefits.' },
          { icon: 'orange', text: '<strong>Recovery matters:</strong> Ensure you have rest days and stretch regularly to prevent injury and improve flexibility.' }
        );
      }

      // Mental health advice
      advice.mental.push(
        { icon: 'green', text: '<strong>Practice mindfulness:</strong> Spend 5-10 minutes daily on meditation or deep breathing to reduce stress and improve focus.' },
        { icon: 'blue', text: '<strong>Social connection:</strong> Reach out to friends or family regularly. Strong social bonds are key to mental well-being.' },
        { icon: 'purple', text: '<strong>Quality sleep:</strong> Aim for 7-9 hours of sleep. Good sleep hygiene improves mood, memory, and overall mental health.' },
        { icon: 'orange', text: '<strong>Digital detox:</strong> Take breaks from screens, especially before bed. Consider a 30-minute screen-free wind-down routine.' }
      );

      return advice;
    }

    function renderAdvice(advice) {
      const categories = ['nutrition', 'physical', 'mental'];
      categories.forEach(cat => {
        const list = document.getElementById(cat + 'Advice');
        list.innerHTML = advice[cat].map(item => `
          <li>
            <div class="bullet ${item.icon}">✓</div>
            <div class="text">${item.text}</div>
          </li>
        `).join('');
      });
    }

    // =====================
    // CHART RENDERING
    // =====================
    function renderChart(history) {
      const svg = document.getElementById('weightChart');
      if (!history || history.length === 0) return;

      const weights = history.map(h => h.weight);
      const minW = Math.min(...weights) - 0.5;
      const maxW = Math.max(...weights) + 0.5;
      const range = maxW - minW;

      const width = 800;
      const height = 200;
      const padding = 40;
      const chartW = width - padding * 2;
      const chartH = height - padding * 2;

      // Generate points
      const points = history.map((h, i) => {
        const x = padding + (i / (history.length - 1)) * chartW;
        const y = padding + chartH - ((h.weight - minW) / range) * chartH;
        return `${x},${y}`;
      }).join(' ');

      // Area points (close the path at bottom)
      const areaPoints = points + ` ${padding + chartW},${padding + chartH} ${padding},${padding + chartH}`;

      // Generate dots
      const dots = history.map((h, i) => {
        const x = padding + (i / (history.length - 1)) * chartW;
        const y = padding + chartH - ((h.weight - minW) / range) * chartH;
        return `<circle class="chart-dot" cx="${x}" cy="${y}" r="5"/>`;
      }).join('');

      // Generate labels
      const labels = history.map((h, i) => {
        const x = padding + (i / (history.length - 1)) * chartW;
        return `<text class="chart-label" x="${x}" y="${height - 10}">${h.date}</text>`;
      }).join('');

      // Y-axis labels
      const yLabels = [];
      for (let i = 0; i <= 4; i++) {
        const val = minW + (range * i / 4);
        const y = padding + chartH - (i / 4) * chartH;
        yLabels.push(`<text class="chart-label" x="30" y="${y + 4}" text-anchor="end">${val.toFixed(1)}</text>`);
      }

      svg.innerHTML = `
        <polygon class="chart-area" points="${areaPoints}"/>
        <polyline class="chart-line" points="${points}"/>
        ${dots}
        ${labels}
        ${yLabels.join('')}
      `;
    }

    // =====================
    // UI UPDATES
    // =====================
    function updateUI(data) {
      // Update basic values
      document.getElementById('heightValue').innerHTML = data.height ? `${data.height}<span class="unit">cm</span>` : '--';
      document.getElementById('weightValue').innerHTML = data.weight ? `${data.weight}<span class="unit">kg</span>` : '--';
      document.getElementById('ageValue').innerHTML = data.age ? `${data.age}<span class="unit">years</span>` : '--';
      document.getElementById('genderValue').innerHTML = data.gender ? data.gender.charAt(0).toUpperCase() + data.gender.slice(1) : '--';

      // Update activity
      document.getElementById('stepsValue').textContent = data.steps ? `${data.steps.toLocaleString()} steps` : 'No data';
      document.getElementById('activeMinutesValue').textContent = data.activeMinutes ? `${data.activeMinutes} min` : 'No data';
      document.getElementById('caloriesBurnedValue').textContent = data.caloriesBurned ? `${data.caloriesBurned} kcal` : 'No data';
      document.getElementById('sleepValue').textContent = data.sleepHours ? `${data.sleepHours} hours` : 'No data';

      // Calculate and update BMI
      const bmi = calculateBMI(data.height, data.weight);
      if (bmi) {
        const bmiInfo = getBMIStatus(bmi);
        document.getElementById('bmiNumber').textContent = bmi;

        const statusEl = document.getElementById('bmiStatus');
        statusEl.textContent = bmiInfo.text;
        statusEl.className = 'bmi-status ' + bmiInfo.status;

        document.getElementById('bmiDescription').textContent = getBMIDescription(bmi);

        // Update circle progress
        const maxBMI = 40;
        const percentage = Math.min(bmi / maxBMI, 1);
        const circumference = 2 * Math.PI * 60; // r=60
        const offset = circumference - (percentage * circumference);
        document.getElementById('bmiProgress').style.strokeDashoffset = offset;
        document.getElementById('bmiProgress').setAttribute('stroke', bmiInfo.color);

        // Update scale marker
        const markerPos = Math.min((bmi / maxBMI) * 100, 100);
        document.getElementById('bmiMarker').style.left = markerPos + '%';
        document.getElementById('bmiMarker').style.borderColor = bmiInfo.color;
      }

      // Calculate and update BMR
      const bmr = calculateBMR(data.weight, data.height, data.age, data.gender);
      if (bmr) {
        document.getElementById('bmrValue').innerHTML = `${bmr.toLocaleString()}<span class="unit">kcal</span>`;
        document.getElementById('bmrSedentary').innerHTML = `${Math.round(bmr * 1.2).toLocaleString()}<span class="unit">kcal</span>`;
        document.getElementById('bmrActive').innerHTML = `${Math.round(bmr * 1.55).toLocaleString()}<span class="unit">kcal</span>`;
      }

      // Update advice
      const advice = generateAdvice(data);
      renderAdvice(advice);

      // Update chart
      const history = data.history && data.history.length > 0 ? data.history : demoHistory;
      renderChart(history);

      // Update timestamp
      document.getElementById('lastUpdated').textContent = 'Last updated: ' + new Date().toLocaleTimeString();
    }

    // =====================
    // DATA FETCHING
    // =====================
    async function loadData() {
      const statusEl = document.getElementById('connectionStatus');

      try {
        const res = await fetch('/data');
        if (!res.ok) throw new Error('Network response was not ok');

        const data = await res.json();
        currentData = { ...currentData, ...data };
        updateUI(currentData);

        statusEl.className = 'connection-status online';
        statusEl.querySelector('span').textContent = 'Live Data';
      } catch (err) {
        console.warn('Failed to fetch data:', err);
        statusEl.className = 'connection-status offline';
        statusEl.querySelector('span').textContent = 'Offline - Using Defaults';

        // Still update UI with current data (or defaults)
        updateUI(currentData);
      }
    }

    // =====================
    // TAB SWITCHING
    // =====================
    document.querySelectorAll('.advice-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.advice-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.advice-content').forEach(c => c.classList.remove('active'));

        tab.classList.add('active');
        document.getElementById(tab.dataset.tab).classList.add('active');
      });
    });

    // =====================
    // INIT
    // =====================
    setInterval(loadData, 1000);
    loadData();
  </script>
</body>
</html>

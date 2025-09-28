#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function checkCommand(command) {
  try {
    execSync(`which ${command}`, { stdio: 'ignore' });
    console.log(`✅ ${command} is installed`);
    return true;
  } catch (error) {
    console.log(`❌ ${command} is NOT installed`);
    console.log(`   → To fix: npm install --save-dev ${command}`);
    return false;
  }
}

function checkVolta() {
  try {
    execSync('volta --version', { stdio: 'ignore' });
    console.log('✅ volta is installed');
    return true;
  } catch {
    console.log('❌ volta is NOT installed');
    console.log('   → To fix: Install volta from https://volta.sh');
    return false;
  }
}

function checkNodeVersion() {
  try {
    const packageJsonPath = path.join(process.cwd(), 'package.json');
    if (!fs.existsSync(packageJsonPath)) {
      console.log('ℹ️  No package.json file found');
      return true;
    }

    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
    const voltaConfig = packageJson.volta;

    if (!voltaConfig || !voltaConfig.node) {
      console.log('ℹ️  No volta.node version specified in package.json');
      return true;
    }

    const expectedVersion = voltaConfig.node;
    const currentVersion = execSync('node -v', { encoding: 'utf8' })
      .trim()
      .replace('v', '');

    if (currentVersion === expectedVersion) {
      console.log(`✅ Node version matches volta config (v${expectedVersion})`);
      return true;
    } else {
      console.log(`❌ Node version mismatch:`);
      console.log(`   - Current: v${currentVersion}`);
      console.log(
        `   - Required: v${expectedVersion} (from package.json volta.node)`,
      );
      console.log(`   → To fix: volta install node@${expectedVersion}`);
      return false;
    }
  } catch (error) {
    console.log('⚠️  Could not verify Node version');
    console.log('   → Check your Node.js installation');
    return false;
  }
}

console.log('Running system checks...\n');

// Check requirements
const checks = [
  { name: 'volta', result: checkVolta() },
  { name: 'black', result: checkCommand('black') },
  { name: 'node version', result: checkNodeVersion() },
];

const failedChecks = checks.filter((c) => !c.result);

if (failedChecks.length > 0) {
  console.log('\n⚠️  Some checks failed:');
  failedChecks.forEach((c) => console.log(`   - ${c.name}`));
  console.log('\n👉 Please fix the issues above before continuing');
  process.exit(1);
} else {
  console.log('\n🎉 All checks passed! You can now proceed with installation.');
}

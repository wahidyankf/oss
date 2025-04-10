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

function checkNvm() {
  if (process.env.NVM_DIR) {
    console.log('✅ nvm is installed (found NVM_DIR)');
    return true;
  }
  try {
    execSync('nvm --version', { stdio: 'ignore' });
    console.log('✅ nvm is installed');
    return true;
  } catch {
    console.log('❌ nvm is NOT installed');
    console.log('   → To fix: Install nvm from https://github.com/nvm-sh/nvm');
    return false;
  }
}

function checkNodeVersion() {
  try {
    const nvmrcPath = path.join(process.cwd(), '.nvmrc');
    if (!fs.existsSync(nvmrcPath)) {
      console.log('ℹ️  No .nvmrc file found');
      return true;
    }

    const expectedVersion = fs.readFileSync(nvmrcPath, 'utf8').trim();
    const currentVersion = execSync('node -v', { encoding: 'utf8' })
      .trim()
      .replace('v', '');

    if (currentVersion === expectedVersion) {
      console.log(`✅ Node version matches .nvmrc (v${expectedVersion})`);
      return true;
    } else {
      console.log(`❌ Node version mismatch:`);
      console.log(`   - Current: v${currentVersion}`);
      console.log(`   - Required: v${expectedVersion} (from .nvmrc)`);
      console.log(
        `   → To fix: nvm install ${expectedVersion} && nvm use ${expectedVersion}`,
      );
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
  { name: 'nvm', result: checkNvm() },
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

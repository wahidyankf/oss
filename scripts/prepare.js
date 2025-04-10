#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function makeExecutable(filePath) {
  try {
    fs.chmodSync(filePath, '755');
    console.log(`✅ Made executable: ${path.basename(filePath)}`);
    return true;
  } catch (error) {
    console.log(`❌ Failed to make executable: ${path.basename(filePath)}`);
    return false;
  }
}

console.log('Preparing husky hooks...\n');

const hooksDir = path.join(process.cwd(), '.husky');
const hookFiles = ['commit-msg', 'pre-commit', 'pre-push'];

hookFiles.forEach((hook) => {
  const hookPath = path.join(hooksDir, hook);
  if (fs.existsSync(hookPath)) {
    makeExecutable(hookPath);
  } else {
    console.log(`⚠️  Hook not found: ${hook}`);
  }
});

console.log('\n🎉 Preparation complete');

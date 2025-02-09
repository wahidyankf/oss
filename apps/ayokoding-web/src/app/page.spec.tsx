import { render, screen } from '@testing-library/react';
import React from 'react';
import Index from './page';

describe('Index', () => {
  it('renders the page', () => {
    render(<Index />);
    expect(screen.getByText(/Hello/i)).toBeInTheDocument();
  });
});

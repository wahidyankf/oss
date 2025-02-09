import { render, screen } from '@testing-library/react';
import React from 'react';
import Home from './page';

describe('Home', () => {
  it('renders the page', () => {
    render(<Home />);
    expect(screen.getByText(/Hello, Ayokoding!/i)).toBeInTheDocument();
  });
});

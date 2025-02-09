import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Home from '../page'

// Disable specific ESLint rules for this file
/* eslint-disable @next/next/no-img-element */

// More robust mock for next/image that handles priority prop
jest.mock('next/image', () => ({
  __esModule: true,
  default: (props: {
    src: string, 
    alt: string, 
    width?: number, 
    height?: number, 
    priority?: boolean,
    className?: string
  }) => {
    const { 
      src, 
      alt, 
      width, 
      height, 
      className, 
      priority,
      ...rest 
    } = props;
    return <img 
      src={src} 
      alt={alt} 
      width={width} 
      height={height} 
      className={className}
      data-priority={priority ? "true" : undefined}
      {...rest} 
    />
  }
}))

describe('Home Page', () => {
  it('renders the home page', () => {
    render(<Home />)
    
    // Check for Hello World text
    const helloText = screen.getByText('Hello, World!')
    expect(helloText).toBeInTheDocument()
  })
})

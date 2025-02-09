import '@testing-library/jest-dom/extend-expect'
import { render, screen } from '@testing-library/react'
import Home from '../page'

/* eslint-disable @next/next/no-img-element */

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
      ...rest 
    } = props;
    return <img 
      src={src} 
      alt={alt} 
      width={width} 
      height={height} 
      className={className}
      {...rest} 
    />
  }
}))

describe('Home Page', () => {
  it('renders the home page', () => {
    render(<Home />)
    
    // Check for Next.js logo
    const nextLogo = screen.getByAltText('Next.js logo')
    expect(nextLogo).toBeInTheDocument()

    // Check for instructions
    const editInstruction = screen.getByText(/Get started by editing/i)
    expect(editInstruction).toBeInTheDocument()

    // Check for deployment and docs links
    const deployLink = screen.getByText('Deploy now')
    const docsLink = screen.getByText('Read our docs')
    expect(deployLink).toBeInTheDocument()
    expect(docsLink).toBeInTheDocument()
  })
})

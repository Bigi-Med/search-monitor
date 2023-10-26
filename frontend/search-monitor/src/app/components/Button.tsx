import React, { FunctionComponent } from 'react'

interface ButtonProps {
    text: string;
    onClick: () => void;
  }

const Button: FunctionComponent<ButtonProps> = ({text , onClick}) => {
    return (
        <button onClick={onClick}
            style={{float: 'right',
                    backgroundColor: '#0056b3',
                    display:'inline-block',
                    color: '#fff',
                    border: 'none',
                    borderRadius: '4px',
                    fontSize: '16px',
                    cursor: 'pointer',
                    marginLeft:'1%'
        }}
        >{text}</button>
    );
};

export default Button;

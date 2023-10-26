import React, { FunctionComponent } from 'react'
import { useState } from 'react'
import styles from './LinkBorder.module.css'

interface LinkBorderProps {
    link: string;
    logo: string;
    children?: React.ReactNode;
    onClick: () => void
}

const LinkBorder: FunctionComponent<LinkBorderProps> = ({link, logo, children,onClick}) => {
    const [showPopup, setShowPopup] = useState(false);

    return (
        <div style={{
                border: '1px solid black',
                background: 'white',
                marginBottom:'10%',
                padding: '30px',
                color:'blue'
        }} onClick={onClick}>
            <a href={link}>{link}</a>
            {children}
        </div>
        );
}
export default LinkBorder
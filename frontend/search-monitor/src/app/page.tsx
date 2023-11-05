'use client'
import Image from 'next/image'
import styles from './page.module.css'
import LinkBorder from './components/LinkBorder'
import axios from 'axios'
import {useState} from 'react'

export default function Home() {
  const [showPopup, setShowPopup] = useState<Boolean>(false);
  const [keywords, setKeywords] = useState<Array<String>>([''])
  const [links, setLinks] = useState<Array<String>>([''])
  const [Loading, setLoading] = useState<Boolean>(false)
  const [emailPopup, setEmailPopup] = useState<Boolean>(false)
  const [email,setEmail] = useState<string>('')
  const [emailConfirmation, setEmailConfirmation] = useState<Boolean>(false)



  const closePopUp = () => {
    setShowPopup(false)
  }

  const parseResponse = (response:any) => {
    let temp_link:Array<String> = []
    let temp_keywords:Array<String> = []

    for (let i = 0; i < response.length; i++) {
      if(response[i]['url'].split('/')[2]=='consent.google.com')
      {
        continue;
      }

      temp_link.push(response[i]['url']);
      temp_keywords.push(response[i]['found'])
    }


    return{
      myKeywords:temp_keywords,
      myLinks:temp_link
    }

  }

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };
  const addEmail = () => {
    setEmailPopup(true)
  }

  const closeEmail = () => {
    setEmailPopup(false)
  }

  const sendEmail = async (email:string) => {
    const response = await axios.get(`http://localhost:5000/email?new=${encodeURIComponent(email)}`);
    setEmailConfirmation(true)
    setEmailPopup(false)


  }

  const getPublisher = async () => {
    setLoading(true)
    const response = await  axios.get('http://localhost:5000/publisher')
     setShowPopup(true)

    let keyword_dict =parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }

  const getGuardian = async () => {
    setLoading(true)
    const response = await  axios.get('http://localhost:5000/guardian')
    setShowPopup(true)

    let keyword_dict = parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }

  const getGoogle = async (link:string) => {
    setLoading(true)
    
    const response = await axios.get(`http://localhost:5000/google?url=${encodeURIComponent(link)}`);

    
    setShowPopup(true)

    let keyword_dict = parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }


  return (
    <main className={styles.main}>
        <div className={styles.pageTitle}>
          <h1>Keyword search</h1>
      </div>
      <div className={styles.container}>
        <div className={styles.leftContainer}>
          {/* <LinkBorder link='https://authorsguild.org/news/?sort=date-DESC' logo='test' onClick={getAuthGuild}>
            </LinkBorder>  */}
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/index.html'  title='Publisher Weekly: ' placeholder='Industry news' onClick={getPublisher}>
          </LinkBorder>
          {showPopup && (
          <div className={styles.popup}>
            {keywords.map((keyword, index) => (
              <div key={index} className={styles.linkKeywords}>
                <br></br>
                <span style={{fontWeight: 'bold', color:'black'}}>Keywords:</span> <span style={{color:'black'}}>{keyword + ' '} </span> <br></br>
                <span style={{fontWeight: 'bold', color:'black'}}>Link: </span> <a style={{color:'blue'}} href={links[index].toString()}>{links[index].substring(0,200)}</a>
              </div>
            ))}
          <button className={styles.closeButton} onClick={closePopUp}>Close</button>
          </div>
          
        )}
        {emailPopup && (
          <div className={styles.popup}>
            <input type="text" placeholder="Enter email"  className={styles.emailInput}  onChange={handleEmailChange} value = {email}/>
            <button className={styles.sendEmail} onClick={() => sendEmail(email)}>Send</button>
            <button className={styles.closeEmail} onClick={closeEmail}>Close</button>
          </div>

          
        )}
          {Loading && (
          <div className={styles.loadingDiv}>
          <img src="/assets/Dual-Ring-removebg.png" className={styles.loadingIcon} alt="Loading" />
        </div>
        )}
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/index.html' title='Publisher Weekly: ' placeholder='Industry news + financial reporting'  onClick={getPublisher}>  
          </LinkBorder>
          <LinkBorder link='https://www.theguardian.com/books'  title='Theguardian: ' placeholder='Books'onClick={getGuardian}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen' title='Google news: ' placeholder='Amazon' onClick={() => getGoogle('https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen' title='Google news: ' placeholder='Kindle direct publishing' onClick={() => getGoogle('https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
        
        </div>
        <div className={styles.rightContainer}>
          <LinkBorder link='https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen'  title='Google news: ' placeholder='Self publishing' onClick={() => getGoogle('https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen'  title='Google news: ' placeholder='AI book lawsuit' onClick={() => getGoogle('https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen' title='Google news: '  placeholder='AI writing lawsuit' onClick={() => getGoogle('https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen' title='Google news: ' placeholder='AI created book' onClick={() => getGoogle('https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen'  title='Google news: ' placeholder=' Author'onClick={() => getGoogle('https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen')}>
          </LinkBorder>

        
        </div>
        <div className={styles.footer}>
        <button className={styles.addEmail} onClick={addEmail}>Add email</button>
          </div>
      </div>

    </main>
  )
}

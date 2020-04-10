; Auto-generated. Do not edit!


(cl:in-package gate_smach-msg)


;//! \htmlinclude CV_msg.msg.html

(cl:defclass <CV_msg> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (center
    :reader center
    :initarg :center
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CV_msg (<CV_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CV_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CV_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gate_smach-msg:<CV_msg> is deprecated: use gate_smach-msg:CV_msg instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <CV_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gate_smach-msg:name-val is deprecated.  Use gate_smach-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <CV_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gate_smach-msg:center-val is deprecated.  Use gate_smach-msg:center instead.")
  (center m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CV_msg>) ostream)
  "Serializes a message object of type '<CV_msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'center) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CV_msg>) istream)
  "Deserializes a message object of type '<CV_msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'center) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CV_msg>)))
  "Returns string type for a message object of type '<CV_msg>"
  "gate_smach/CV_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CV_msg)))
  "Returns string type for a message object of type 'CV_msg"
  "gate_smach/CV_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CV_msg>)))
  "Returns md5sum for a message object of type '<CV_msg>"
  "f97c3665b94139c47928a4e2b9761f46")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CV_msg)))
  "Returns md5sum for a message object of type 'CV_msg"
  "f97c3665b94139c47928a4e2b9761f46")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CV_msg>)))
  "Returns full string definition for message of type '<CV_msg>"
  (cl:format cl:nil "string name~%bool center~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CV_msg)))
  "Returns full string definition for message of type 'CV_msg"
  (cl:format cl:nil "string name~%bool center~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CV_msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CV_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'CV_msg
    (cl:cons ':name (name msg))
    (cl:cons ':center (center msg))
))

    def visitIf(self,ctx,o):
        if_exprCode, if_exprType = ctx.expr.accept(self, Access(o.frame, o.sym, False))
        if ctx.estmt:
            labelElse = o.frame.getNewLabel()
            labelExit = o.frame.getNewLabel()
            self.emit.printout(if_exprCode)
            self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))
            ctx.tstmt.accept(self, o)
            self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))
            self.emit.printout(self.emit.emitLABEL(labelElse, o.frame))
            ctx.estmt.accept(self, o)
            self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
        else:
            labelExit = o.frame.getNewLabel()
            self.emit.printout(if_exprCode)
            self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
            ctx.tstmt.accept(self, o)
            self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))